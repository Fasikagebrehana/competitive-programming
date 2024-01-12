class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count_t, count_f = 0, 0
        l = 0
        max_confusion = 0
        for r in range(len(answerKey)):
            if answerKey[r] == 'T':
                count_t += 1
            if answerKey[r] == 'F':
                count_f += 1
            min_count = min(count_t, count_f)
            while min_count > k:
                if answerKey[l] == 'T':
                    count_t -= 1
                if answerKey[l] == 'F':
                    count_f -= 1
                min_count = min(count_t, count_f)
                l += 1
            max_confusion = max(max_confusion, r - l + 1)
        return max_confusion