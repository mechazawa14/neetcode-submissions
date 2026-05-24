# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# till now we did only dfs now wer doing bfs for the first time , for dfs we used stack
# here we use queue , deque to be precise 

# Popping an element from the front of a deque (double-ended queue) has a time complexity 
# of \(O(1)\).Unlike standard arrays or lists, where removing the first element requires 
# shifting every subsequent element (an \(O(n)\) operation), a deque is specifically 
# engineered to handle insertions and removals at both ends in constant time.

# If you use a standard Python list as a queue and do list.pop(0) to remove the first 
# element, Python has to shift all remaining elements left by one index. 
# This takes \(O(N)\) time. If you do this for every node, your code becomes slow 
# (\(O(N^2)\)).A deque is engineered to allow you to pop from the front using .popleft() 
# in \(O(1)\) constant time—no matter how big the queue gets. That is why we use it.

from collections import deque 

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        queue = deque([root])
        result  = []
        while queue:
            levelsize = len(queue)
            current_level = []
            for _ in range(levelsize):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
        return result
        