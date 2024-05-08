class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = {}
        sorted_score = sorted(score, reverse = True)

        for i in range(len(score)):
            if i == 0:
                rank[sorted_score[i]] = "Gold Medal"
            elif i == 1:
                rank[sorted_score[i]] = "Silver Medal"
            elif i == 2:
                rank[sorted_score[i]] = "Bronze Medal"
            else:
                rank[sorted_score[i]] = str(i+1)
        ans = [0] * len(score)
        for key, val in rank.items():
            idx = score.index(key)
            ans[idx] = val

        return ans