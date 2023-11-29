class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10 and x >= 0:
            return True
        else:
            n = str(x)
            for i in range(len(n) // 2):
                if n[i] != n[-i - 1]:
                    return False
            return True
        
        