# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root :
                return False 
        def issametree (p, q):
                if p and not q:
                        return False 
                if not p and q :
                        return False 
                if not p and not q :
                        return True 
                if p.val != q.val :
                        return False 
                return issametree(p.left, q.left) and issametree(p.right, q.right)
        if issametree(root,subRoot):
                return True 
        return self.isSubtree(root.left, subRoot ) or self.isSubtree(root.right , subRoot )
        

        

                