class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = nums[0]
        curr = nums[0]
        for i in range(1, len(nums)):
            curr += nums[i]
            ans = max(ans, math.ceil(curr / (i+1)) )
        return ans