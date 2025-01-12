from collections import deque

class TreeNode(): 
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def VertTraversal(root):
    
    widthMap = {}
    widthQueue = deque()
    widthQueue.append((root, 0))

    while(widthQueue):
        currTuple = widthQueue.popleft()
        if currTuple[0].left:
            widthQueue.append((currTuple[0].left, currTuple[1] - 1))

        if currTuple[0].right:
            widthQueue.append((currTuple[0].right, currTuple[1] + 1))


        if currTuple[1] in widthMap.keys():
            widthMap[currTuple[1]].append(currTuple[0].val)
        else: 
            widthMap[currTuple[1]] = [currTuple[0].val]
    
    sortedMapKeys = sorted(widthMap.keys())
    finalList = []
    for i in sortedMapKeys:
        finalList.append(widthMap[i])
    
    return finalList



root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

print(VertTraversal(root))
