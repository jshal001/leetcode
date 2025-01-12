class Node: 
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = Node(0, 0), Node(0,0)
        self.head.prev, self.tail.next = self.tail, self.head


    #helper functions to remove and insert
    def insert(self, node):

        #insert at head
        self.head.prev.next, node.prev = node, self.head.prev
        node.next, self.head.prev = self.head, node


    
    def remove(self, node):
        #remove at tail
        node.prev.next, node.next.prev = node.next, node.prev

    #Return the value of the key if the key exists, otherwise return -1
    #O(1)
    def get(self, key):
        #first check if key exists in cache 
        if(key in self.cache):
            #remove and insert so its at the beginning 
            currNode = self.cache[key]
            self.remove(currNode)
            self.insert(currNode)
            return currNode.val

        return -1

    #Update value of key if key exists, else add key value pair. 
    #if exceeds capacity after operation,
    #O(1)
    def put(self, key, value):
        if(key in self.cache):
            self.remove(self.cache[key])
        
        #add new node to the cache
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        #check for capacity 
        if(len(self.cache) > self.capacity):
            lru = self.tail.next
            self.remove(lru)
            self.cache.pop(lru.key)
            
        
            



        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)