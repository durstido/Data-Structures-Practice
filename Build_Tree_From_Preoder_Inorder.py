# Definition for a binary tree node.
class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
            
class Solution(object):
    def buildTree(self, preorder, inorder):
        
        if (len(preorder)==0):
            return None
        
        root = Node(preorder[0], None, None)
        
        if(len(preorder)==1):
            return root
        
        LLength = self.findLeftSubTreeLength(inorder, preorder[0])
        RLength = len(preorder) - LLength - 1
        
        if (LLength!=0):
            root.left = self.buildTree(preorder[1:LLength+1], inorder[:LLength]) 
        if (RLength!=0):
            root.right = self.buildTree(preorder[1+LLength:], inorder[1+LLength:])			
        return root 
    
    def findLeftSubTreeLength(self, inorder, root):
        length=0
        for i in range(len(inorder)):
            if (inorder[i] == root):
                return length
            length +=1 