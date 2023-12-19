class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = 2 * k
        if len(s) < k:
            return s[::-1]
        elif len(s) > k and len(s) <= n:
            return s[k-1::-1] + s[k:]
        else:
            s = s[:k][::-1] + s[k:n] + self.reverseStr(s[n:], k)
            return s