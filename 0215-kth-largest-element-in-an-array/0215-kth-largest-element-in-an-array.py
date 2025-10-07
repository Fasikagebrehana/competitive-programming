class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, -num)
        answer = 0
        while heap and k > 0:
            answer = heappop(heap)
            k -= 1
        return -answer