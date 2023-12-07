class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i <= n:
            if i not in nums:
                return i
            i += 1
        return 0