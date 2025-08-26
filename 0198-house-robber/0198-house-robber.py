class Solution:
    def rob(self, nums: List[int]) -> int:
        # we have 2 choices either we add the current value and move to i+2
        # or try the next i+1

        memo = {}
        def dp(i):
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]
            memo[i] = max((nums[i] + dp(i+2)), dp(i+1))

            return memo[i]
        return dp(0)