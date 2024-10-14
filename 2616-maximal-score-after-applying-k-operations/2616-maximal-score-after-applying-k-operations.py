class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        score = 0
        for i in range(len(nums)):
            heappush(heap, -(nums[i]))
        
        while k > 0:
            num = heappop(heap)
            # print(num)
            score += -(num)
            heappush(heap, (num//3))
            # print(ceil(num/3))
            k-= 1
        
        return score