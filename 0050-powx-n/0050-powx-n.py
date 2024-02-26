class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if x == 0:
        #     return 0
        def helper(x, n):
            if n == 0:
                return 1
            res = helper(x, n//2)
            if n % 2 == 0:
                ans =  res * res
            else:
                ans = res * res * x
            return ans
        ans = helper(x,abs(n))
        return ans if n >= 0 else 1/ans