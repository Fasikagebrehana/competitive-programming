class Solution:
    def isHappy(self, n: int) -> bool:
        def squareSum(num):
            total_sum = 0
            while num > 0:
                digit = num % 10
                total_sum += digit ** 2
                num //= 10
            return total_sum
        
        seen = set()
    
        while n != 1 and n not in seen:
            seen.add(n)
            n = squareSum(n)
    
        return n == 1