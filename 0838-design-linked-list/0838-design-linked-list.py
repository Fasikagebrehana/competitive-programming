class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = None
    def get(self, index: int) -> int:
        currnode = self.head
        indx = 0
        while currnode:
            if indx == index:
                return currnode.val
            currnode = currnode.next
            indx += 1
        return -1

    def addAtHead(self, val: int) -> None:
        newnode = Node(val)
        newnode.next = self.head
        self.head = newnode

    def addAtTail(self, val: int) -> None:
        newnode = Node(val)
        if not self.head:
            self.head = newnode
            return
        currnode = self.head
        while currnode.next:
            currnode = currnode.next
        currnode.next = newnode

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
        newnode = Node(val)
        if index == 0:
            newnode.next = self.head
            self.head = newnode
            return
        currnode = self.head
        prev = None
        idx = 0
        while currnode and idx < index:
            prev = currnode
            currnode = currnode.next
            idx += 1
        if idx == index:
            prev.next = newnode
            newnode.next = currnode
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        currnode = self.head
        prev = None
        idx = 0
        while currnode and idx < index:
            prev = currnode
            currnode = currnode.next
            idx += 1
        if idx == index and currnode:
            prev.next = currnode.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)