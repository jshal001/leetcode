from dataclasses import dataclass,field
import heapq

@dataclass(order=True)
class Node():
    sort_index: int = field(init=False, repr=False)
    key: str
    value: int

    def __post_init__(self): 
        self.sort_index = 0 - self.value

    
class TaskQueue:
    def __init__(self, tasks=None,n=0):
        self.n = n
        self.maxHeap = []
        self.tasks = tasks
        self.timeout = {}
        self.taskMap = {}

        #populate task map
        for i in tasks: 
            if i not in self.taskMap.keys():
                self.taskMap[i] = 1
            else:
                self.taskMap[i] += 1
        
        #populate list
        for key,value in self.taskMap.items():
            self.add(key,value)

    def add(self, key, value):
        # Create a KeyValuePair object and append it to the deque
        heapq.heappush(self.maxHeap,Node(key, value))

    def Tick(self):
        for i in self.timeout.copy():
            self.timeout[i] -= 1
            if self.timeout[i] < 0:
                heapq.heappush(self.maxHeap,Node(i[0], i[1]))
                del self.timeout[i] 
    def addToTimeOut(self, nodeTuple):
        self.timeout[nodeTuple] = self.n
        print("Current Timeout: ", self.timeout)

    def getLeastIntervals(self):
        countIntervals = 0
        while(len(self.maxHeap) or len(self.timeout)):
            #while all tasks are in timeout
            while(len(self.maxHeap) == 0):
                countIntervals += 1
                self.Tick()
                print("idle")
            #if given task is in timeout, wait till it's not
            currNode = heapq.heappop(self.maxHeap)
            print(currNode)
            
            currNode.value -= 1
            if(currNode.value != 0):
                #add node to timeout
                self.addToTimeOut((currNode.key, currNode.value))
            countIntervals += 1
            self.Tick()
            print(currNode.key)
        return countIntervals




def leastintervals(tasks, n):   
    scheduledTasks = TaskQueue(tasks, n)

    return scheduledTasks.getLeastIntervals()
    
    
tempTasks = ["A","A","A","B","B","B"]
n = 3

print(leastintervals(tempTasks, n))




    