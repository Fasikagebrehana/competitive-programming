class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(i):
            
            if i == len(nums) - 1:
                return 0
            if i in memo:
                return memo[i]

            count = -inf
            for j in range(i+1, len(nums)):
                if -target <= nums[j] - nums[i] <= target:
                    count = max(count, 1 + dp(j))
            memo[i] = count
            return memo[i]
        
        max_jump = dp(0)
        return -1 if max_jump == -inf else max_jump