class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        maximized_sum = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            maximized_sum += nums[i]
        return maximized_sum