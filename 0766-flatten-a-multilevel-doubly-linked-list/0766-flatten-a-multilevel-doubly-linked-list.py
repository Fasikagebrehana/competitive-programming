"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # if node has a child, node's next will be saved for future and continue with the child node
        store = []
        curr = head
        
        def linkedlist(node):
            nonlocal store
            # last = None
            while node:
                if node.child:
                    if node.next:
                        store.append(node.next)
                    node.next = node.child
                    node.child.prev = node
                    node.child = None
                    node = node.next
                    linkedlist(node.child)
                else:
                    node = node.next
            if store:
                prevnext = store.pop()
                tail = head
                while tail and tail.next:
                    tail = tail.next
                
                prevnext.prev = tail
                tail.next = prevnext
                linkedlist(prevnext)
        
        linkedlist(curr)
        return head
        
