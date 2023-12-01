import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1 or n == 3:
            return True
        while True:
            n = n / 3
            if n == 3:
                return True
            if n < 3:
                return False