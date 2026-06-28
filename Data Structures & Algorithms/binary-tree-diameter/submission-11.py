# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxdiam  = 0 #gonna be getting updated as we traverse the tree 
        # clearly we feel the need of an helper func as we need to find the maxdia
        # assuming each node as hinge 
        def maxpathforeachnode(node):
            if not node :
                return 0
            leftpathlength = maxpathforeachnode(node.left)
            rightpathlength = maxpathforeachnode(node.right)
            self.maxdiam = max(self.maxdiam, leftpathlength + rightpathlength)
            return max(leftpathlength, rightpathlength)+1 
        maxpathforeachnode(root)
        return self.maxdiam