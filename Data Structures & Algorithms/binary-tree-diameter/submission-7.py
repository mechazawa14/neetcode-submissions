# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxdiam  = 0 
        def maxDepth(node):
                if not node :
                        return 0
                leftdepth  = maxDepth (node.left)
                rightdepth  = maxDepth(node.right)
                self.maxdiam  = max(self.maxdiam, leftdepth + rightdepth)
                
                return 1+ max(leftdepth , rightdepth)
        maxDepth(root)
        return self.maxdiam
