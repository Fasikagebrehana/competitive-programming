class Solution:
    def canAliceWin(self, n: int) -> bool:
        x = 10
        while n >= 0 and x > 0:
            if n < x:
                if x %2 == 0: 
                    return False
                else:
                    return True
            n -= x
            x -= 1
        