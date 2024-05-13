class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        store = {}
        def dp(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if (i, j) not in store:
                if text1[i] == text2[j]:
                    store[(i, j)] = 1 + dp(i+1, j+1)
                else:
                    store[(i, j)] = max(dp(i+1, j), dp(i, j+1))
            return store[(i, j)]
        return dp(0, 0)