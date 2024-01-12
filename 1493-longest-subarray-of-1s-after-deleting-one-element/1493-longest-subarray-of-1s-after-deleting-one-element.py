class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        l = 0
        count = 0
        if len(nums) <= 2:
            return len(nums)-1
        if sum(nums) == 0:
            return 0
        for r in range(len(nums)):
            if nums[r] == 0:
                count += 1
            while count > 1:
                if nums[l] == 0:
                    count -= 1
                l += 1
            ans = max(ans, r - l- 1)
                
        return ans+1