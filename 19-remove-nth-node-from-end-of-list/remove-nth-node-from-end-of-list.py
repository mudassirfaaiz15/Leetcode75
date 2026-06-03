# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # Move fast pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers
        while fast:
            slow = slow.next
            fast = fast.next

        # Remove nth node
        slow.next = slow.next.next

        return dummy.next