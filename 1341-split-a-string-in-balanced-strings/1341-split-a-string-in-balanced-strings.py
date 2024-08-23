class Solution:
    def balancedStringSplit(self, s: str) -> int:
        countR, countL = 0, 0
        ans = 0
        for st in s:
            if countR == countL:
                ans += 1
            if st == 'R':
                countR += 1
            else:
                countL += 1
        return ans