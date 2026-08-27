"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        hashmap = {}
        og_head = head

        while head:
            hashmap[head] = Node(head.val)
            head = head.next
        
        head = og_head

        while head:
            hashmap[head].next = hashmap[head.next] if head.next else None
            hashmap[head].random = hashmap[head.random] if head.random else None
            head = head.next
        
        return hashmap[og_head]