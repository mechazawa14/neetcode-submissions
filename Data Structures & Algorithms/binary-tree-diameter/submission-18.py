# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxdiam = 0
        def maxpathforeachnode(node):
            if not node :
                return 0 
            leftmaxdepth = maxpathforeachnode(node.left)
            rightmaxdepth  = maxpathforeachnode(node.right)
            self.maxdiam = max(self.maxdiam, leftmaxdepth + rightmaxdepth)
            return max(leftmaxdepth, rightmaxdepth)+1
        maxpathforeachnode(root)
        return self.maxdiam
