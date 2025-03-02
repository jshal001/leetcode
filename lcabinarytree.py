from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
#***************** O(N) solution **************************************
# def getNode(root: 'TreeNode', target:int):
#     if root == None: 
#         return None
    
#     if root.val == target: 
#         return root

#     leftTree = getNode(root.left, target)
#     if leftTree is not None:
#         return leftTree
#     rightTree = getNode(root.right, target)
#     if rightTree is not None: 
#         return rightTree


# def getNodeAncestors(root: 'TreeNode', target: int): 
        
#     if root == None: 
#         return None
    
#     if root.val == target: 
#         return str(root.val) + ","
        
#     leftTree = getNodeAncestors(root.left, target)
#     if leftTree is not None:
#         return leftTree + str(root.val) + ","
#     rightTree = getNodeAncestors(root.right, target)
#     if rightTree is not None: 
#         return rightTree + str(root.val) + ","


# def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#     #pull ancestors of both p and q and remove trailing comma
#     q_Ancestry = getNodeAncestors(root, q.val).rstrip(',').split(',')
#     p_Ancestry = getNodeAncestors(root, p.val).rstrip(',').split(',')

#     #filter check only for elements present in both lists
#     common_ancestors = []

#     for val in q_Ancestry: 
#         if val in p_Ancestry:
#             common_ancestors.append(val)
    
#     return getNode(root, int(common_ancestors[0]))

#*********************************************************************************************    


#faster solution
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        
    if not root: 
        return None
    
    if root == q or root == p:
        return root
    
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)

    if left and right: 
        return root
    
    return left if left else right



root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

print(lowestCommonAncestor(root,root.right.left,root.right.right))