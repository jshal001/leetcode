class TreeNode:
    def __init__(self, val=0, left=None, right=None): 
        self.val = val
        self.left = left
        self.right = right

class Solution: 
    def invertTree(self, root): 
        """
        :type root: TreeNode
        :rtpe: TreeNode
        """
        
        if not root: 
            return 
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp

        
        return root

# Time Complexity: O(n)
# Space Complexity: O(h) s.t. h = height of tree 