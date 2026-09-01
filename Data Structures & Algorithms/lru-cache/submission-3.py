class Node:
    def __init__(self, key = 0, value=0):
        self.key = key
        self.val = value
        self.prev = self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hashmap = {}

        self.lru = Node(0, 0)
        self.mru = Node(0, 0)
        self.lru.nxt, self.mru.prev = self.mru, self.lru
    
    def insert(self, node):
        prev = self.mru.prev
        nxt = self.mru
        
        prev.nxt = node
        node.prev = prev

        node.nxt = nxt
        nxt.prev = node
    
    def remove(self, node):
        prev = node.prev
        nxt = node.nxt

        prev.nxt = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        node = self.hashmap[key]
        self.remove(node)
        self.insert(node)
        
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove(node)
        node = Node(key, value)
        self.hashmap[key] = node
        self.insert(node)

        if len(self.hashmap) > self.cap:
            lru = self.lru.nxt
            self.remove(lru)
            del self.hashmap[lru.key]


