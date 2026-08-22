# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.wrongheightspotted = 0
        if not root:
            return True 
        def heightdiffforanode(node):
            if not node:
                return 0
            leftheight = heightdiffforanode(node.left)
            rightheight = heightdiffforanode(node.right)
            height_diff = abs(leftheight - rightheight)
            if height_diff > 1:
                self.wrongheightspotted = 1
            return max(leftheight, rightheight)+1
        heightdiffforanode(root)
        if self.wrongheightspotted == 1:
            return False 
        return True 

        
            
            


