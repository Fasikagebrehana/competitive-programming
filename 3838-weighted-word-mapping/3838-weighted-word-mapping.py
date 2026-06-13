class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = ""

        for word in words:
            summ = 0
            for ch in word:
                summ += weights[ord(ch) - ord('a')]
            temp = chr(ord('a') + (26 - (summ % 26)) - 1)
            # print(chr(temp))
            result += temp
        return result
            