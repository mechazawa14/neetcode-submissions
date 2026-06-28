# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxdiam  = 0 
        def maxpathlengthforanode(node):
            if not node :
                return 0
            leftpathmaxlength = maxpathlengthforanode(node.left)
            rightpathmaxlength = maxpathlengthforanode(node.right)
            self.maxdiam = max(self.maxdiam , leftpathmaxlength+rightpathmaxlength)
            return max(maxpathlengthforanode(node.left), maxpathlengthforanode(node.right))+1
        maxpathlengthforanode(root)
        return self.maxdiam
