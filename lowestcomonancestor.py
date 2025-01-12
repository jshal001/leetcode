def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    large = max(p.val, q.val)
    small = min(p.val, q.val)


    while(root): 
        #if root value is less then both values in the right subtree 
        if (root.val < small): 
            root = root.right
        elif (root.val > large): 
            root = root.left
        #otherwise,  small <= root.val <= large
        else: 
            return root 
        
    
