class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        st = list(s)
        for i in range(len(s)):
            st[indices[i]] = s[i]
        return ''.join(st)