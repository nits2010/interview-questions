# Enter your code here. Read input from STDIN. Print output to STDOUT

import heapq
class Agent:
    def __init__(self, name, limit=2):
        self.name = name
        self.limit = limit
        self.load = 0
        self.last_assigment = 0

# custome exception
class AgentAssigmentLoadException:
    def __init__(self, message):
        self.message = message
     
# Time: O(C*logN)
# Space : O(N)
class AssignmentSystem:
    def __init__(self, agents): # initialize 
        self.agents = {} # map
        self.heap = []
        self.time = 0
    
        for name in agents:
            agent = Agent(name)
            self.agents[name] = agent
            heapq.heappush(self.heap, (agent.load, agent.last_assigment, name))
    
    def set_limit(agent_name, limit):
        agent = self.agents[agent_name]
        agent.limit = limit
    
    # Time: O(C*logN)
    def assign(self, conversations_ids):
        result = []
        
        for c_id in conversations_ids:
            temp = []
            assgined = None
            
            while self.heap:
                load, last_assigment, name = heapq.heappop(self.heap)
                agent = self.agents[name]
                
                if agent.load < agent.limit:
                    assgined = agent
                    break
                else:
                    temp.append((load, last_assigment, name))
            
            for item in temp:
                heapq.heappush(self.heap, item)
            
            
            if not assgined:
                raise AgentAssigmentLoadException("Agents are busy....")
                
            
            self.time +=1 
            assgined.load +=1
            assgined.last_assigment = self.time
            
            heapq.heappush(self.heap, (assgined.load, assgined.last_assigment, assgined.name))
            result.append(assgined.name) 
        
        
        
        
        return result
    
    
