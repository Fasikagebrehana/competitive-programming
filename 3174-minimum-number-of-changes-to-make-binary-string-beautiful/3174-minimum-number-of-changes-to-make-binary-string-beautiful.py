class Solution:
    def minChanges(self, s: str) -> int:
        ans = 0
        left, right = 0, 1
        while right < len(s):
            if s[left] != s[right]:
                ans += 1
            right += 1
            left = right
            right += 1
        return ans