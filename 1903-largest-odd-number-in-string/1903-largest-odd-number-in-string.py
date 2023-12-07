class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        
        i = len(num) - 1
        for i in range(len(num)-1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[:i+1] 
        return ""