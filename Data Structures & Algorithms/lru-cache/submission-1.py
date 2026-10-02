class Node:
    def __init__(self, key, val):
        self.key = key      # Needed to delete from hashmap
        self.val = val
        self.prev = None    # Previous node
        self.next = None    # Next node


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}     # key → node

        # Dummy boundaries: left = LRU, right = MRU
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        # Empty list: left ⇄ right
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        # Connect node's neighbors
        prev = node.prev
        nxt = node.next

        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        # Insert node right before right (MRU)
        prev = self.right.prev
        nxt = self.right

        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:

            # Accessed = move to MRU
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:

        # Remove old node if key exists
        if key in self.cache:
            self.remove(self.cache[key])

        # Create new node and add to hashmap
        self.cache[key] = Node(key, value)

        # New item = MRU
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:

            # Remove LRU
            lru = self.left.next
            self.remove(lru)

            # Remove LRU from hashmap
            del self.cache[lru.key]