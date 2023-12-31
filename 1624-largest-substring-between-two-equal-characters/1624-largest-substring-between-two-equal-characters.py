class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dic = {}
        ans = []
        max_diff = -1
        for i, ch in enumerate(s):
            if ch in dic:
                dif = i - dic[ch][0] - 1
                max_diff = max(max_diff, dif)
            else:
                dic[ch] = [i]
        return max_diff