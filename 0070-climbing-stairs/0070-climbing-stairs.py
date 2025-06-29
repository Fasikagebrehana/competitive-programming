class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        ans = 0
        def dp(steps):
            nonlocal ans

            if steps == 1:
                return 1
            if steps == 2:
                return 2
            if steps in memo:
                return memo[steps]
            
            ans = dp(steps - 1) + dp(steps - 2)
            memo[steps] = ans
            return ans

        
        
        return dp(n)