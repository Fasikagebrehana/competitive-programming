class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        count = 1
        max_count = 1
        num = sorted(nums)
        l, r = 0, 1
        while r < len(nums):
            if num[r] -  num[l] == 1:
                count += 1
                max_count = max(max_count, count)
            elif num[r] != num[l]:
                count = 1
            l += 1
            r += 1
        return max_count
        
        