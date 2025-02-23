from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
        
def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if root == None: 
        return []
    
    treeQ = deque()
    treeQ.append(root)

    traversal = []
    
    while treeQ:
        currLevel = []
        while treeQ:
            currLevel.append(treeQ.popleft())

        for i in range(len(currLevel)):
            currNode = currLevel[i]
            #add child nodes to queue
            if currNode.left:
                treeQ.append(currNode.left)
            
            if currNode.right: 
                treeQ.append(currNode.right)

            #replace current node with its value
            currLevel[i] = currNode.val

        traversal.append(currLevel)
     

    
    return traversal
        



root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

print(levelOrder(root))
