class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # using dp bottom up 
        # starting from the last index, check each slice if its true

        dp = [False] * (len(s) + 1)
        dp[-1] = True
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if (i + len(word)) <= len(s):
                    if word == s[i: i + len(word)]:
                        # example 1: checking code(s[4:8]) == wordDict[1]
                        dp[i] = dp[i+len(word)]
                if dp[i] == True:
                    break

        # if s can be segmented from wordDict dp[0] will be true
        return dp[0] 