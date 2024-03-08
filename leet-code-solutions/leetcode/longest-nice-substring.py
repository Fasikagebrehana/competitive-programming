class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        strings = set(s)
        temp = ""
        if not s:
            return ""
        for i in range(len(s)):
            if s[i].swapcase() in strings:    
                temp += s[i]
            else:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                return max(left, right, key=len)
        return temp
