class Solution:
    def nthUglyNumber(self, n: int) -> int:
        minHeap = []
        heappush(minHeap, 1)
        currentUgly = 0
        primeFactors = [2, 3, 5]
        visited = set({1})
        for i in range(2, n+1):
            currentUgly = heappop(minHeap)
            for num in primeFactors:
                new = num * currentUgly
                if new not in visited:
                    visited.add(new)
                    heappush(minHeap, new)
        return minHeap[0]