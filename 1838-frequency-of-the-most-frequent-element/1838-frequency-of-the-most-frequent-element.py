class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        l = 0
        i = 0
        nums.sort()
        ans = 0
        x = 0
        while i < len(nums):
            x += nums[i]
            if (nums[i] * (i-l+1)) - x <= k:
                ans = max(ans, (i-l+1))
            else:
                while l < i and (nums[i] * (i-l+1)) - x > k:
                    x -= nums[l]
                    l += 1
            i += 1
        return ans
             