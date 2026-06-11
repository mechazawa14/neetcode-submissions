# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # so here basically wkt , every path will have a turning node ,
        # for that turning node we calculate the same as prev problem 
        # for every node as turning node we find its max path length 
        # which is max depth of its left child + max depth of its right child 
        # for ex if max depth of left child of a node  = 2 and max depth of 
        # the right child of the node  = 2 then length of the path through node 
        # is 2+2 =4 , so we find this for every node assuming it as the turning node 
        # and like this we will compare path for all nodes and show max diameter
        self.maxdiameter = 0
        # were making a default initial variable as maxdiameter which we 
        # assume 0 initially , the fact that we did self. means we made it as a global 
        # variable , which means it will be useful in all the functions we make 
        # in the class , like maxdepth as we see  
        #literally previous program code 
        def maxdepth(node): 
            if not node :
                return 0
            leftmaxdepth = maxdepth(node.left)
            rightmaxdepth = maxdepth(node.right)
            self.maxdiameter = max(self.maxdiameter , leftmaxdepth+rightmaxdepth)

            return max(leftmaxdepth , rightmaxdepth)+1
        maxdepth(root)

        return self.maxdiameter
            
            