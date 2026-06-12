# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxdiam  = 0 
        def maxdepth(node):
            if not node :
                return 0 
            leftmaxdepth  = maxdepth(node.left)
            rightmaxdepth = maxdepth(node.right)
            self.maxdiam  = max(self.maxdiam, leftmaxdepth + rightmaxdepth)
            return 1+ max(leftmaxdepth , rightmaxdepth)

        maxdepth(root)
        return self.maxdiam 
        