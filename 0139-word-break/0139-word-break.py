class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # using dp bottom up 
        # starting from the last index, check each slice if its true

        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if s[j:i] in wordDict and dp[j]:
                    dp[i] = True
                    break

        # if s can be segmented from wordDict dp[0] will be true
        # print(dp)
        return dp[len(s)] 