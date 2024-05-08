class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        arr = []
        for i in range(len(profits)):
            arr.append((capital[i], profits[i]))
        arr.sort()
        heap = []
        i = 0
        while k > 0:
            while i < len(arr):
                if arr[i][0] <= w:
                    heappush(heap, -arr[i][1])
                    i += 1
                else:
                    break
            if heap:
                w += -(heappop(heap))
            k -= 1
        return w