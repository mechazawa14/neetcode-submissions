# Imagine a shelf that only holds 2 books.You put in Book A. 
# Shelf: [A]You put in Book B. Shelf: [A, B] (B is the newest).
# You look at Book A (get). Now A is "fresh," so you move it to the front.
#  Shelf: [B, A]You want to put in Book C. The shelf is full! Who do you kick out?
#   You kick out Book B because it’s the "Least Recently Used." Shelf: [A, C]


# To get an \(O(1)\) (instant) speed, we have a conflict:A Dictionary is instant
#  for finding things, but it has no "order." It doesn't know who is old or new.
#  A Linked List is great for order, but to find a specific node, 
#  you have to walk through the whole thing (\(O(n)\)).The Solution: We use both. 
#  The Dictionary stores the Key, and the Value is a pointer to the Node inside
#   a Doubly Linked List.

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key -> node
        
        # Sentinels/Dummies to avoid None checks
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # HELPER: You add this yourself to handle the "unplugging"
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # HELPER: You add this to handle the "moving to front"
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key]) # Take out
            self.insert(self.cache[key]) # Put at MRU (right)
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            # The LRU node is the one right after our Left dummy
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
