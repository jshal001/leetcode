from typing import Optional
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def printGraph( node: Optional['Node']): 
    graphQ = deque()
    graphQ.append(node)
    visited = []

    while graphQ:
        currNode = graphQ.popleft()

        print("Node: " + str(currNode.val))
        print("Neighbors:")
        for i in currNode.neighbors: 
            print(i.val)

            if i.val not in visited: 
                graphQ.append(i)
        
        visited.append(currNode.val)

def cloneGraph( node: Optional['Node']) -> Optional['Node']:
    if not node: 
        return node
        
    visited = []

    qOld = deque()
    nodeMap = {}
    qOld.append(node)
    nodeMap[node.val] = Node(node.val)
    visited.append(node.val)
    

    while qOld: 
        #create new node with value and it's neighbors
        currOld = qOld.popleft()

        for i in currOld.neighbors:
            if i.val in nodeMap.keys():
                nodeMap[currOld.val].neighbors.append(nodeMap[i.val])
            else: 
                newChild = Node(i.val)
                nodeMap[i.val] = newChild
                nodeMap[currOld.val].neighbors.append(nodeMap[i.val])
        
            if i.val not in visited:
                qOld.append(i)
                visited.append(i.val)
        
                
        
        
        

    # self.printGraph(nodeMap[node.val])
    
    return nodeMap[node.val]


#test
N1 = Node(1)
N2 = Node(2)
N3 = Node(3)
N4 = Node(4)

N1.neighbors.extend([N2, N4])
N2.neighbors.extend([N1, N3])
N3.neighbors.extend([N2, N4])
N4.neighbors.extend([N1, N3])

printGraph(cloneGraph(N1))