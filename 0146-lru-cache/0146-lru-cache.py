class LinkedList:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.head = None
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = LinkedList(0, 0)
        self.right = LinkedList(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.store = {}
    
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev


    def get(self, key: int) -> int:
        if key in self.store:
            self.remove(self.store[key])
            self.insert(self.store[key])
            return self.store[key].val
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.remove(self.store[key])
        self.store[key] = LinkedList(key, value)
        self.insert(self.store[key])
        if len(self.store) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.store[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)