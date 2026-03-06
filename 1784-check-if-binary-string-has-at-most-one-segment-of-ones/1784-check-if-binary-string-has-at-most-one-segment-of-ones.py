class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        flag = False
        if len(s) == 1 and s[0] == '1':
            return True
        for i in range(1, len(s)):
            if s[i-1] == '0' and s[i] == '1':
                if flag:
                    return False
            if s[i-1] == '1' and s[i] == '0' and not flag:
                flag = True
        return True
                    
            
        return False