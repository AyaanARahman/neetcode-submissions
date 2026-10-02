class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #map the key to the node

        self.left = Node(0,0)
        self.right = Node(0,0)

        #Left = LRU
        self.left.next = self.right

        #right = most recent
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next, nxt.prev = nxt, prev
        

    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)

        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            #remove from list and evict from LRU cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
