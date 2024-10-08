class Solution:
    def minSwaps(self, s: str) -> int:
        min_swap = 0
        open, closed = 0, 0
        for i in range(len(s)):
            if s[i] == '[':
                open += 1
            else:
                closed += 1

            if closed > open:
                min_swap += 1
                closed -= 1
                open += 1
        return min_swap