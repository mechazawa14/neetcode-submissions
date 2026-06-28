# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.wrongheightspotted = 0
        def checkheightforeachnode(node):
            if not node :
                return 0
            leftheightyet  = checkheightforeachnode(node.left)
            rightheightyet  = checkheightforeachnode(node.right)
            if abs(leftheightyet - rightheightyet) > 1:
                self.wrongheightspotted = 1
                return 0 
            return max(leftheightyet, rightheightyet)+1 
        checkheightforeachnode(root)
        if self.wrongheightspotted == 1:
            return False 
        return True