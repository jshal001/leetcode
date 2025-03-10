
from typing import Optional,List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    
    roots = preorder

    def Traverse(subTree: List[int]) -> Optional[TreeNode]:
        

        #first element of preorder list is root, but first check if preorder is empty
        if len(roots) == 0 or len(subTree) == 0: 
                return None
        
        
        root = TreeNode(roots.pop(0))
        

        #left sub tree is all left of root value in inorder list
        rootIndex = subTree.index(root.val)
        root.left = Traverse(subTree[0:rootIndex])
        root.right = Traverse(subTree[rootIndex + 1: len(inorder)])

        return root
    return Traverse(inorder)

#taken from stackoverflow
def PrintTree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1  
    nlevels = height(root)
    width =  pow(2,nlevels+1)

    q=[(root,0,width,'c')]
    levels=[]

    while(q):
        node,level,x,align= q.pop(0)
        if node:            
            if len(levels)<=level:
                levels.append([])
        
            levels[level].append([node,level,x,align])
            seg= width//(pow(2,level+1))
            q.append((node.left,level+1,x-seg,'l'))
            q.append((node.right,level+1,x+seg,'r'))

    for i,l in enumerate(levels):
        pre=0
        preline=0
        linestr=''
        pstr=''
        seg= width//(pow(2,i+1))
        for n in l:
            valstr= str(n[0].val)
            if n[3]=='r':
                linestr+=' '*(n[2]-preline-1-seg-seg//2)+ '¯'*(seg +seg//2)+'\\'
                preline = n[2] 
            if n[3]=='l':
               linestr+=' '*(n[2]-preline-1)+'/' + '¯'*(seg+seg//2)  
               preline = n[2] + seg + seg//2
            pstr+=' '*(n[2]-pre-len(valstr))+valstr #correct the potition acording to the number size
            pre = n[2]
        print(linestr)
        print(pstr)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

PrintTree(buildTree(preorder, inorder))