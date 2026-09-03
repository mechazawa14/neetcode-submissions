# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxdepth  = 0 
        def maxpathwithnode(node):
            if not node :
                return 0 
            leftmaxdepth = maxpathwithnode(node.left)
            rightmaxdepth = maxpathwithnode(node.right)
            
            self.maxdepth = max(self.maxdepth, leftmaxdepth + rightmaxdepth)
            return max(maxpathwithnode(node.left), maxpathwithnode(node.right))+1
        maxpathwithnode(root)
        return self.maxdepth
             