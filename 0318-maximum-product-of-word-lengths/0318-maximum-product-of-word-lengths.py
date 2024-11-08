class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                for ch in words[i]:
                    if ch in words[j]:
                        break
                else:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans