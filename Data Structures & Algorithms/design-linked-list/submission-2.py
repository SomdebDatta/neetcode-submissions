class ListNode:
    def __init__(self, val=0, nxt=None, prev=None):
        self.val = val
        self.nxt = nxt
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.left = ListNode()
        self.right = ListNode()
        self.left.nxt = self.right
        self.right.prev = self.left
        self.length = 0

    def get(self, index: int) -> int:
        if index > self.length - 1:
            return -1
        node = self.left
        for idx in range(index + 1):
            node = node.nxt
        
        return node.val

    def addAtHead(self, val: int) -> None:
        head = self.left.nxt
        new_node = ListNode(val)
        self.left.nxt = new_node
        new_node.prev = self.left
        new_node.nxt = head
        head.prev = new_node
        self.length += 1
        

    def addAtTail(self, val: int) -> None:
        tail = self.right.prev
        new_node = ListNode(val)
        self.right.prev = new_node
        tail.nxt = new_node
        new_node.prev = tail
        new_node.nxt = self.right
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        new_node = ListNode(val)
        node_at_idx = self.left
        for idx in range(index):
            node_at_idx = node_at_idx.nxt
        
        node_after_idx = node_at_idx.nxt

        node_at_idx.nxt = new_node
        new_node.prev = node_at_idx

        new_node.nxt = node_after_idx
        node_after_idx.prev = new_node
        self.length += 1



    def deleteAtIndex(self, index: int) -> None:
        if index > self.length - 1:
            return

        node_at_idx = self.left
        for idx in range(index + 1):
            node_at_idx = node_at_idx.nxt
        
        prev = node_at_idx.prev
        nxt = node_at_idx.nxt
        prev.nxt = nxt
        nxt.prev = prev
        self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)