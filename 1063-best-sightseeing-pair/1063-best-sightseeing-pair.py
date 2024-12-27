class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0
        maxx = values[0]
        for i in range(1, len(values)):
            max_score = max(max_score, maxx + values[i] - i)
            maxx = max(maxx, values[i] + i)
        return max_score