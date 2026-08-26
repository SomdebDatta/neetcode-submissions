# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None

        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        reverse_half = prev
        while head and reverse_half.next:
            nxt = head.next
            reverse_half_nxt = reverse_half.next
            head.next = reverse_half
            reverse_half.next = nxt
            head = nxt
            reverse_half = reverse_half_nxt
