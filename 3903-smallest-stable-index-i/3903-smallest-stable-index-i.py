class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            if max(nums[:i+1]) - min(nums[i:]) <= k:
                # print(nums[i])
                return i
        return -1