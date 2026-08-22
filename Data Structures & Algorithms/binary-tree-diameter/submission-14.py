# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxdiam = 0
        def maxpathforanode (node):
            if not node :
                return 0 
            leftmaxdepth = maxpathforanode(node.left)
            rightmaxdepth = maxpathforanode(node.right)
            self.maxdiam = max(self.maxdiam , leftmaxdepth + rightmaxdepth)
            return max(leftmaxdepth, rightmaxdepth)+1
        maxpathforanode(root)
        return self.maxdiam
    


            

            
            
