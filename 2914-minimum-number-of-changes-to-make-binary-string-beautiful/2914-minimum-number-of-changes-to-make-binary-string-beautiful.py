class Solution:
    def minChanges(self, s: str) -> int:
        min_change = 0
        i = 0
        while i < len(s) - 1:
            if s[i] != s[i+1]:
                min_change += 1
                i += 2
            else:
                i += 2
        # print(min_change)
        return min_change