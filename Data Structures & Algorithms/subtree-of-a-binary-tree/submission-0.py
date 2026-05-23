# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base Case: If we scan all the way to the bottom and find nothing, it's False
        if not root:
            # An empty main tree can never contain a subtree!
            return False
        
        # 1. Check if the tree starting right here is an exact twin of subRoot
        if self.isSameTree(root, subRoot):
            return True
        
        # 2. If it's not a twin here, tell the left and right branches to keep scanning!
        # We use 'or' because the match only needs to be found on ONE of the sides.
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    # --- YOUR TRUSTY WEAPON FROM PROBLEM 1 ---
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
