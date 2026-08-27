# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return
        length = 0

        og_head = head

        while head:
            length += 1
            head = head.next
        
        if length == 1:
            return

        if length == n:
            return og_head.next
        ct = 0
        head = og_head
        # print(ct, length, n)
        while ct != length - n - 1:
            ct += 1
            head = head.next
        

        remove_node = head.next

        if remove_node.next:
            head.next = remove_node.next
        else:
            head.next = None
        
        return og_head