class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = (10 ** 9) + 7
        if n % 2 == 0:
            even = n // 2
        else:
            even = (n // 2)  + 1
        odd = n // 2
        def power(x, n):
            if n== 1:
                return x
            if n == 0:
                return 1
            
            if n % 2 == 0:
                val = power(x, n//2)
                return (val ** 2) % (mod)
            else:
                val = power(x, n//2)
                return ((val ** 2) * x) % (mod)
        return (power(4, odd) if power(4, odd) else 1) * (power(5, even) ) % mod 
        