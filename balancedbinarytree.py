# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root):
        if root == None:
            return True
        leftH = self.getHeight(root.left)
        rightH = self.getHeight(root.right)
        if leftH == -1 or rightH == -1:
            return False
        else: 
            return abs(leftH - rightH) <= 1
         

        
    def getHeight(self, currNode): 
        if(currNode == None):
            return 0
        leftH, rightH = self.getHeight(currNode.left), self.getHeight(currNode.right)
        if(abs(leftH - rightH) > 1 or leftH == -1 or rightH == -1):
            return -1

        return max(leftH, rightH) + 1 
    
    
        
solution = Solution()
node1 = TreeNode(1)
node2 = TreeNode(2, None, TreeNode(5,None, TreeNode(6)))
root = TreeNode(3, node1, node2)

print(solution.isBalanced(root))

