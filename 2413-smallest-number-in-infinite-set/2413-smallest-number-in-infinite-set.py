class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.curr = 1

    def popSmallest(self) -> int:
        if self.heap:
            return heapq.heappop(self.heap)
        else:
            self.curr += 1
            return self.curr - 1



    def addBack(self, num: int) -> None:
        if num not in self.heap and num < self.curr:
            heapq.heappush(self.heap, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)