class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        summ = sum(nums)
        left_sum = 0
        valid = 0
        for i in range(len(nums)-1):
            left_sum += nums[i]
            summ -= nums[i]
            if left_sum >= summ:
                valid += 1

        return valid