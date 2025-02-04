class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        for i in range(len(nums)):
            summ = nums[i]
            curr = nums[i]
            j = i+1
            while j < len(nums) and nums[j] > curr:
                curr = nums[j]
                summ += nums[j]
                j += 1
            max_sum = max(max_sum, summ)
        return max_sum
