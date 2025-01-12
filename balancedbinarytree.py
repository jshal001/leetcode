# Definition for a binary tree node.
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def isBalanced(self, root):
        return (self.Height(root) >= 0)
    
    def Height(self, root):
        if root is None:
            return 0
        
        [leftheight, rightheight] = self.Height(root.left), self.Height(root.right)

        if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:
            return -1
        
        return max(leftheight, rightheight) + 1  
    
        
solution = Solution()
node1 = TreeNode(1)
node2 = TreeNode(2, None, TreeNode(5,None, TreeNode(6)))
root = TreeNode(3, node1, node2)

print(solution.isBalanced(root))
print(node1)
