class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_avg = sum(nums[:k])
        max_avg = curr_avg
        for i in range(k, len(nums)):
            curr_avg += nums[i]
            curr_avg -= nums[i - k]
            max_avg = max(max_avg,curr_avg)
        return max_avg/k