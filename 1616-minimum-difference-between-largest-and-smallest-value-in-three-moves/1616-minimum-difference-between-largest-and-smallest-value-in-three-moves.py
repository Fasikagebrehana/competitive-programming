class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort(reverse = True)
        rev = sorted(nums)
        return min((nums[3] - nums[-1]), rev[-1] - rev[3], rev[-2] - rev[2], rev[-3] - rev[1])