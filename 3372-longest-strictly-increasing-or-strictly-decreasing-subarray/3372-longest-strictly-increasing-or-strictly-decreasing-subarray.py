class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        max_increasing = 1
        max_decreasing = 1
        curr = nums[0]
        for i in range(len(nums)):
            j = i+1
            curr = nums[j-1]
            while j < len(nums) and nums[j] > curr:
                max_increasing = max(max_increasing, j - i + 1)
                curr = nums[j]
                j += 1
            
            j = i+1
            curr = nums[j-1]
            while j < len(nums) and nums[j] < curr:
                max_decreasing = max(max_decreasing, j - i + 1)
                curr = nums[j]
                j += 1
        return max(max_increasing, max_decreasing)
        