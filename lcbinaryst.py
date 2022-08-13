# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val < q.val:
            min, max = p.val, q.val
        else:
            min, max = q.val, p.val

        
        while(True):
            if min <= root.val <= max:
                return root
            elif min > root.val:
                root = root.right
            else: 
                root = root.left




solution = Solution()

p = TreeNode(2)
q = TreeNode(1)
root = p
root.left = q

res = solution.lowestCommonAncestor(root, p, q)

print(res.val)

#Time Complexity: O(h) st h = height of tree
#Space Complexity: O(1)
