class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        for i in range(len(nums)):
            heappush(heap, (nums[i], i))

        while k > 0:
            temp, i = heappop(heap) 
            temp *= multiplier
            nums[i] = temp
            heappush(heap, (temp, i))
            k -= 1
        return nums