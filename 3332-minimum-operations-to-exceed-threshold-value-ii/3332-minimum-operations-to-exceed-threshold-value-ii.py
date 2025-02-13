class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, num)
        
        operations = 0
        while len(heap) >= 2:
            x = heappop(heap)
            y = heappop(heap)
            if x >= k:
                return operations
            temp = x * 2 + y
            heappush(heap, temp)
            operations += 1
        return operations