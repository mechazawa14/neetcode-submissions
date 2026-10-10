# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxdiam =  0 
        def maxpathwitheverynodeaspivot(node):
            if not node :
                return 0 
            leftmaxpath = maxpathwitheverynodeaspivot(node.left)
            rightmaxpath = maxpathwitheverynodeaspivot(node.right)
            self.maxdiam = max(self.maxdiam,  leftmaxpath + rightmaxpath) 
            return max(leftmaxpath, rightmaxpath) + 1 
        maxpathwitheverynodeaspivot(root)
        return self.maxdiam