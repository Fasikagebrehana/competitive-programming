class Solution:
    def minimumSteps(self, s: str) -> int:
        count_zero = 0
        ans = 0
        for right in range(len(s)-1, -1, -1):
            if s[right] == '0':
                count_zero += 1
            if s[right] == '1':
                ans += count_zero
        return ans
            