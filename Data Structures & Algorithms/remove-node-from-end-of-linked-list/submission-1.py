# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# the thing that makes the problem tricky is that had we were to delete 
# frlm the beginning just travel n steps and do node.next = node.next.next and
# we're good , but here we need to delete from backwards whic is not easy as 
# we ought to travel list only once .

# Instead of different speeds, we use a fixed gap.
# Put two pointers (fast and slow) at a Dummy Node before the head.
# Give fast a head start of \(n\) steps
# Now, move both fast and slow forward at the same speed (1 step at a time).
# Because the gap between them is exactly \(\), when fast reaches the very 
# last node,slow will be standing right before the node we want to delete.

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy  = ListNode(0, head)
        slow = fast = dummy 

        # 1. Give 'fast' the head start
        for _ in range(n):
            fast = fast.next 

        # 2. Move together until 'fast' is at the last node
        while fast.next :
            slow = slow.next 
            fast  = fast.next 
            
        # 3. atp, the gap between fast and slow is exactly n means slow.next is 
        # at the node we need to delete so skip the slow 
        slow.next = slow.next.next 
        return dummy.next





