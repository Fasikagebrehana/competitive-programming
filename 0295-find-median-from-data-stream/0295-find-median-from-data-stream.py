class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        # we'll append all to the min heap to avoid comparing it to everytime then pop and add the minimum of them all to the max_heap
        heappush(self.min_heap, num)
        heappush(self.max_heap, -heappop(self.min_heap))
        # if the length of the max_heap > the min_heap 
        if len(self.max_heap) > len(self.min_heap) +1:
            heappush(self.min_heap, -heappop(self.max_heap))
            

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            num1, num2 = heappop(self.min_heap), -heappop(self.max_heap)
            heappush(self.min_heap, num1)
            heappush(self.max_heap, -num2)
            return (num1 + num2) / 2
        elif len(self.min_heap) > len(self.max_heap):
            temp = heappop(self.min_heap)
            heappush(self.min_heap, temp)
            return temp
        else:
            temp = heappop(self.max_heap)
            heappush(self.max_heap, temp)
            return -temp


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()