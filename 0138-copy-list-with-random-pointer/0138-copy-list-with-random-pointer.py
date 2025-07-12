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
            return None
        copy = Node(head.val)
        # print(copy)
        store = {}
        curr = head
        while curr:
            temp = Node(curr.val)
            store[curr] = temp
            curr = curr.next
        
        for key, val in store.items():
            val.next = store[key.next] if key.next else None
            val.random = store[key.random] if key.random else None
        return store[head]