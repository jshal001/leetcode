# Definition for a binary tree node.
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution():
    def traverseTree(self, root):
        #base case, if reaches end, return -1 and true 
        if root == None:
            return -1, True
        
        #ask left subtree for height and isbalanced? 
        [leftHeight, isBalanced] = self.traverseTree(root.left)
        #check if balanced, if not, bubble up false
        if not isBalanced:
            return -1, False
        
        [rightHeight, isBalanced] = self.traverseTree(root.right)
        if not isBalanced:
            return -1, False
        
        #now that we've retrieved both left and right height, do calculation
        if(abs(leftHeight - rightHeight) > 1):
            return -1, False
        else: 
            return max(leftHeight, rightHeight) + 1, True


            
      
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        [height, isBalanced] = self.traverseTree(root)

        return isBalanced
        
solution = Solution()
node1 = TreeNode(1)
node2 = TreeNode(2, None, TreeNode(5,None, TreeNode(6)))
root = TreeNode(3, node1, node2)

print(solution.isBalanced(root))
print(node1)

#Time Complexity: O(n)
#Space Complexity: O(h) - call stack