class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = 0
        n = len(cardPoints)
        win_sum = sum(cardPoints[:(n - k)])
        total = sum(cardPoints)
        max_score = total - win_sum
        for right in range(n - k, n):            
            win_sum -= cardPoints[left]
            win_sum += cardPoints[right]
            max_score = max(max_score, total - win_sum)
            left += 1
        return max_score
        