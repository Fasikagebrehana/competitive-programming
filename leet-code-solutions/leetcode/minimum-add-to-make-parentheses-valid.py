class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        countCloseP = s.count(')')
        countOpenP = 0
        ans = 0
        for c in s:
            if c == '(':
                if countCloseP <= 0:
                    ans += 1
                else:
                    countCloseP -= 1
                countOpenP += 1
            elif c == ')':
                if countOpenP <= 0:
                    ans += 1
                    countCloseP -= 1
                else:
                    countOpenP -= 1
                # 
        return ans