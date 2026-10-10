# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isnotbalanced = 0 
        def checkbalanceforeachnode(node):
            if not node :
                return True 
            leftheight = checkbalanceforeachnode(node.left)
            rightheight = checkbalanceforeachnode(node.right)
            height =  abs(leftheight - rightheight)
            if height > 1 :
                self.isnotbalanced = 1
            return max(leftheight, rightheight) +  1
        checkbalanceforeachnode(root)
        return self.isnotbalanced == 0
            

