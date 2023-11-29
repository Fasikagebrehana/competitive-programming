class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10 and x >= 0:
            return True
        else:
            n = str(x)
            if n == n[::-1]:
                return True
            else:
                return False
            
                
        
        