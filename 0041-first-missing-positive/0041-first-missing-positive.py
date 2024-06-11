class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        n = 1
        for i in range(len(nums)):
            if nums[i] == n:
                n += 1
        return n