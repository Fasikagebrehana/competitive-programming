class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        symmetric_int = 0
        for num in range(low, high+1):
            s = str(num)
            if len(s) % 2 == 0:
                n = len(s)
                summ1 = 0
                summ2 = 0
                for i in range(n//2):
                    summ1 += int(s[i])
                
                for j in range(n//2, n):
                    summ2 += int(s[j])
                if summ1 == summ2:
                    symmetric_int += 1
        return symmetric_int