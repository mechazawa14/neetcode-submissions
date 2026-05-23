# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def finddepths(node):
                if not node :
                        return 0 
                leftdepth  = finddepths(node.left)
                if leftdepth == -1 :
                        return -1 
                rightdepth  = finddepths(node.right)
                if rightdepth == -1:
                        return -1
                if abs(leftdepth - rightdepth) > 1 :
                        return -1
                return max(leftdepth, rightdepth)+1 
        if finddepths(root) == -1:
                return False 
        return True
        
        



        