class Solution:
    def climbStairs(self, n: int) -> int:
        store = {}
        def climb(n):
            if n < 3:
                return n
            if n not in store:
                store[n] = climb(n-1) + climb(n-2)
            return store[n]
        ans = climb(n)
        return ans