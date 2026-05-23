# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diametermax = 0 
        def find_diameter_at_each_node(node): #helper fucntion
                if not node :
                        return 0 
                left_depth  = find_diameter_at_each_node(node.left)
                right_depth = find_diameter_at_each_node(node.right)
                current_path_length = left_depth + right_depth 
                self.diametermax = max(self.diametermax , current_path_length)
                return max(left_depth, right_depth)+1

        find_diameter_at_each_node(root)
        return self.diametermax

                
                