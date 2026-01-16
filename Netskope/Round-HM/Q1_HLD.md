Question Type: HLD
Question: 
You have 2 API based systems at your disposal.
 Googledrive drive
 Malware system.

 Given these two systems, design a system which would tag a file uploaded to google drive if it is a malware as malware.
 Considerations:
 The files incoming to Google drive can vary. From 1 million in 5 seconds to 1 per second. 
 We do not have control over the scale of incoming files into google drive.
 The Malware should be detected as fast as possible the overall ecosystem allows and tagged malware in google drive.
 Both of these systems are SAAS services.

 What do you have:
 Google APIs
 1. Google Drive API to get list of file ids uploaded/modified given start time t1 and end time t2
 2. Google drive API to get content about file
 3. Google drive API to add label to a file , given a file ID

 Malware APIs
 4. Malware API to give a verdict yes or no, given checksum of a file.


 ----------------------------------------------------------------------------------------

 Drivers are 
 - GDrive & Malware API 
   - GDrive Api [Perfom action]


Solution: 
This is a classic asynchronous processing challenge at scale. As a Senior Staff Engineer, my primary concerns here are **durability**, **backpressure management**, and **idempotency**. Since we have no control over the ingress rate (from 1 to 200k+ RPS), we cannot use a synchronous "push" model. We must build a resilient, event-driven pipeline.

---

## High-Level Design Strategy

To handle the extreme variance in load, we will decouple the **Discovery** of files from the **Processing** of files using a distributed message queue.

### 1. The Component Stack

* **Discovery Service (Poller):** Since we only have "List API" (t1 to t2), this service will run on a schedule (e.g., every 5-10 seconds) to fetch new file IDs and push them into a buffer.
* **Message Broker (e.g., Kafka or Pub/Sub):** Acts as a shock absorber for the "1 million in 5 seconds" bursts.
* **Scanning Workers:** A fleet of auto-scaling consumers that pull from the queue, fetch file content, compute checksums, and call the Malware API.
* **Tagging Service:** Updates the Google Drive label based on the verdict.

---

## Technical Workflow

| Step | Action | Logic/Optimization |
| --- | --- | --- |
| **1. Poll** | Discovery Service queries Google Drive API for files modified between `last_poll_time` and `now`. | We use "checkpointing" in a database to ensure no time gaps are missed. |
| **2. Enqueue** | File IDs are pushed to a **High-Throughput Queue**. | We use the File ID as the partitioning key to ensure we don't process the same file twice simultaneously. |
| **3. Process** | Worker fetches file metadata/content via Google API. | **Optimization:** Stream the file content to compute the checksum locally; don't store it to disk. |
| **4. Check** | Call Malware API with the computed Checksum. | If the Malware API is also a SaaS, we must implement **Rate Limiting** and **Circuit Breakers**. |
| **5. Label** | If Malware = True, call Google Drive API to add the "Malware" label. | Use an exponential backoff strategy for API failures. |

---

## Handling the "Scale Constraints"

### Managing the Burst (1M files / 5s)

A standard API poller might struggle with a million-file response.

* **Pagination:** We must aggressively paginate the Google Drive List API.
* **Fan-out:** The Discovery Service will split large lists into smaller batches (e.g., 1000 IDs per message) to allow the Worker fleet to parallelize the workload immediately.

### Minimizing Latency

To detect malware "as fast as possible":

* **Parallel Downloads:** Workers should use asynchronous I/O to download file chunks and pipe them directly into a hashing function (SHA-256).
* **Result Caching:** We should maintain a local **LRU Cache** (Redis) of "Checksum -> Verdict". If a million users upload the exact same malicious file, we only call the Malware SaaS once.

### Efficiency & Costs

* **The "Double-Check" Avoidance:** Before processing, we check if the file already has a "Scanned" or "Malware" label to avoid redundant API calls and costs.

---

## Proposed Architecture Diagram

### Key Resilience Patterns

1. **Dead Letter Queues (DLQ):** If a file fails to be downloaded or the Malware API times out after 3 retries, the message moves to a DLQ for manual inspection or later retry.
2. **Backpressure:** If the Malware API starts returning `429 Too Many Requests`, our Workers will slow down their consumption rate from the queue.
3. **Idempotency:** Since we are polling by time ranges, there is a risk of overlapping results. The system will use the `FileID` as a unique key in our tracking DB to ensure we don't trigger multiple scans for one upload.

**Would you like me to drill down into the database schema for the Discovery Service's checkpointing or discuss the specific scaling policy for the Workers?**
