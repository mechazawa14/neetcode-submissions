# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.iswrongheight  = 0 
        def  heightdiffofnode(node):
                if not node:
                        return True 
                leftheight  = heightdiffofnode(node.left)
                rightheight = heightdiffofnode(node.right)
                if abs(leftheight - rightheight) > 1 :
                        self.iswrongheight  = 1 
                return max(leftheight, rightheight) +1 
        heightdiffofnode(root)
        if self.iswrongheight == 1:
                return False 
        return True
