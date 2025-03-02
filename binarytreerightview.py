from typing import Optional,List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    heightMap = {}
    rightView = []

    def dfs(node, depth): 
        if not node: 
            return None
        if depth not in heightMap: 
            heightMap[depth] = []
            
        heightMap[depth].append(node.val)

        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)
    
    dfs(root, 0)
    
    for key in heightMap.keys():
        rightView.append(heightMap[key][(len(heightMap[key]) - 1)])
    
    return rightView
        
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

print(rightSideView(root))