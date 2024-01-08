class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr, maxsubstr = 0, 0
        count = {}
        start = 0
        for i in range(len(s)):
            st = s[i]
            if st in count and count[st] >= start:
                start = count[st] + 1
            count[st] = i
            curr = i - start + 1
            maxsubstr = max(maxsubstr, curr)
        return maxsubstr