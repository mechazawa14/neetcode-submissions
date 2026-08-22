# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxdiam  = 0
        def maxpathlengthfornode(node):
            if not node :
                return 0 
            leftmaxdepth = maxpathlengthfornode(node.left)
            rightmaxdepth = maxpathlengthfornode(node.right)
            self.maxdiam = max(self.maxdiam , leftmaxdepth+rightmaxdepth)
            return max(maxpathlengthfornode(node.left), maxpathlengthfornode(node.right))+1
        maxpathlengthfornode(root)
        return self.maxdiam

            

            
            
