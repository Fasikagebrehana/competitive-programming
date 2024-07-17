class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr, maxsubstr = 0, 1
        count = {}
        if len(s) == 0:
            return 0
        # start = 0
        # for i in range(len(s)):
        #     st = s[i]
        #     if st in count and count[st] >= start:
        #         start = count[st] + 1
        #     count[st] = i
        #     curr = i - start + 1
        #     maxsubstr = max(maxsubstr, curr)
        # return maxsubstr
        l, r = 0, 1
        count[s[l]] = 1
        while l < len(s) and r < len(s):
            if s[r] not in count:
                count[s[r]] = 1
                r += 1
                curr = r - l
            else:
                del count[s[l]]
                
                l += 1
            maxsubstr = max(maxsubstr, curr)
        return maxsubstr
            