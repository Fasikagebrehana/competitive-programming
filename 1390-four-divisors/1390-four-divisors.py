class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            summ = 0
            count = 0

            n = 1
            while n*n <= num:
                # if its divisible by n == divisor
                if num % n == 0:
                    count += 1
                    summ += n

                    d = num // n
                    if d != n:
                        count += 1
                        summ += d
                    
                    if count > 4:
                        break
                n += 1
            
            if count == 4:
                ans += summ
        return ans