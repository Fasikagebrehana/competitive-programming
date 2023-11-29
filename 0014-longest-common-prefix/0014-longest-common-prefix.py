class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        st = sorted(strs)
        start = st[0]
        last = st[-1]
        
        for i in range(min(len(start), len(last))):
            if start[i] != last[i]:
                return ans
            ans += start[i]
        return ans