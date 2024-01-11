class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        left, right = 0, 0
        if sum(nums) < target:
            return 0
        s = 0
        while right < len(nums):
            s += nums[right]
            while s >= target:
                min_length = min(min_length, right - left + 1)
                s -= nums[left]
                left += 1
            right += 1
        return min_length
                