# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.wrongheightspotted  =  0 
        def traverseallnodes(node):
            if not node :
                return True  
            leftdepthofnode = traverseallnodes(node.left)
            rightdepthofnode = traverseallnodes(node.right)
            heightdiff = abs(leftdepthofnode - rightdepthofnode)
            if heightdiff > 1 :
                self.wrongheightspotted = 1
            return max(traverseallnodes(node.left),traverseallnodes(node.right))+1 
        traverseallnodes(root)
        if self.wrongheightspotted == 0:
            return True  
        else:
            return False 


            

        
            
            


