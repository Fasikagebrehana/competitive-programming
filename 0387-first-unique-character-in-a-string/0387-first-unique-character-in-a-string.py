class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]] += 1
            else:
                dic[s[i]] = 1
        for i in range(len(s)):
            if dic[s[i]] == 1:
                a = str(s[i])
                return s.index(a)
        return -1