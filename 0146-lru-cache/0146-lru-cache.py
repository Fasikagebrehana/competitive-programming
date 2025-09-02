# on the listnode we need this to create a new node which have a next, prev, key and value
class ListNode:
    def __init__(self, key, value):
        self.next = None
        self.prev = None
        self.key = key
        self.value = value

class LRUCache:
    # for the recent access use linkedlist
    # 1: ListNode()
    # for the count part use dictionary 
    # we need two functions remove for removing a node and to add a node to the listnode
    # ??when do we create head and tail 

    def __init__(self, capacity: int):
        self.store = {}
        self.capacity = capacity
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head


        
    def remove(self, key):
        node = self.store[key]
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add(self, key, val):
        # we create a new listnode for the 
        #  value we create a new node with the key and value
        # assign the prev to the tail.prev and the next to tail
        newnode = ListNode(key, val)
        newnode.prev = self.tail.prev
        self.tail.prev.next = newnode
        newnode.next = self.tail
        self.tail.prev = newnode
        self.store[key] = newnode
        


    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        self.remove(key)
        value = self.store[key].value
        del self.store[key]
        self.add(key, value)
        return value
        

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.remove( key)

        self.add(key, value)

        if len(self.store) > self.capacity:
            # print(self.head.next.key)
            temp = self.head.next
            self.head.next = temp.next
            temp.next.prev = self.head
            # print(temp)
            print(self.tail.key)
            if temp.key in self.store:
                del self.store[temp.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)