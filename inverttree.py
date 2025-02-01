# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root == None or (root.left == None or root.right == None): 
        return root
    invertTree(root.left)
    invertTree(root.right)

    temp = root.left 
    root.left = root.right
    root.right = temp

    return root
        



currTree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)),TreeNode(7, TreeNode(6), TreeNode(9)))

invertTree(currTree)