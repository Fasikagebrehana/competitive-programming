class Solution:
    def maxPower(self, s: str) -> int:
        ans = 0
        count = 1
        if len(s) == 1:
            return count

        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                count += 1
            else:
                count = 1
            ans = max(ans, count)
            
        return ans