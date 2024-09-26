class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = deque()
        self.k = k  

    def insertFront(self, value: int) -> bool:
        if len(self.queue) < self.k:
            self.queue.appendleft(value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if len(self.queue) < self.k:
            self.queue.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.queue:
            self.queue.popleft()
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if self.queue:
            self.queue.pop()
            return True
        else:
            return False
        

    def getFront(self) -> int:
        if self.queue:
            return self.queue[0]
        else:
            return -1

    def getRear(self) -> int:
        if self.queue:
            return self.queue[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.queue:
            return False
        else:
            return True

    def isFull(self) -> bool:
        if len(self.queue) < self.k:
            return False
        else:
            return True


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(self.k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()