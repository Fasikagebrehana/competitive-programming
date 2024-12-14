class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        store = {}
        def dp(i, j):
            if i == len(s):
                return True
            if j >= len(t) and i < len(s):
                return False
            if i >= len(s) or j >= len(t):
                return
            
            if (i, j) not in store:
                if s[i] == t[j]:
                    store[(i, j)] = dp(i+1, j+1)
                else:
                    store[(i, j)] = dp(i, j+1)
            return store[(i, j)]
        return dp(0, 0)            