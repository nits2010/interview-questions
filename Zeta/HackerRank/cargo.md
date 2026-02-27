Based on the images provided, here is the full extraction of the **Java: Cargo Management** coding problem.

---

## **Problem Description: Java: Cargo Management**

A shipping company needs a cargo management application. You are required to implement two classes, `Package` and `Cargo`, along with their respective interfaces.

### **1. The `Package` Class**

Create the `Package` class and implement the `IPackage` interface with the following properties:

* `id` (int)
* `name` (String)
* `weight` (int)
* `length` (int)
* `width` (int)
* `height` (int)

### **2. The `Cargo` Class**

Create the `Cargo` class and implement the `IShipping` interface:

* **Field:** Declare a field of `List` to store the packages.
* **Methods to implement:**
* `addPackage(IPackage package)`: Adds a package to the list.
* `removePackage(int id)`: Removes a package from the list based on its ID.
* `calculateTotalCost()`: Returns the total cost of shipping for all packages in the list.
* `categoryPrices()`: Returns a `Map<String, Integer>` representing the weight category and the total shipping cost for each category.
* **Small:** Weight<= 1 AND Length<=30 AND Width<=30 AND Height<=30
* **Medium:** Weight<=3 AND Length<=60 AND Width<=60 AND Height<=60
* **Large:** Any package that does not fit "Small" or "Medium" criteria.


* `packageList()`: Returns a `Map<String, Integer>` with each unique package name as the key and the count of those packages as the value.



### **3. Shipping Cost Logic**

The cost to ship an item is based on the product of Volume ($L \times W \times H$):

* If L * W * H <= 100,000: **Cost = 10**
* If 100,000 < L * W * H <= 500,000$: **Cost = 20**
* If 500,000 > L * W * H: **Cost = 30**

---

### **Example Scenario**

**Input Packages:**

1. Package-1: ID=1, W=3, L=46, Wth=40, H=23
2. Package-2: ID=2, W=2, L=54, Wth=68, H=37
3. Package-3: ID=3, W=2, L=65, Wth=45, H=60
4. Package-4: ID=4, W=3, L=20, Wth=50, H=11
5. Package-5: ID=5, W=1, L=29, Wth=22, H=9
6. Package-6: ID=6, W=1, L=11, Wth=16, H=31

**Cost Calculation Example:**
For Package ID 1: $46 * 40 * 23 = 42,320. Since this is <= 100,000, the cost is **10**.

**Sample Output:**

```text
Total Cost: 80
Medium Category Price: 30
Large Category Price: 40
Small Category Price: 10
Package-1 (1 units)
Package-2 (1 units)
... [and so on for all packages]

```

---

### **Sample Input (Case 1)**

```text
3
1 Package-1 1 4 40 35
2 Package-2 2 62 3 7
3 Package-3 3 46 12 56

```

### **Sample Output (Case 1)**

```text
Total Cost: 30
Large Category Price: 20
Medium Category Price: 10
Package-1 (1 units)
Package-2 (1 units)
Package-3 (1 units)

```

---