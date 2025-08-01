class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # using two pointers on each dictionary words
        dictionary.sort()
        answer = ""
        for word in dictionary:
            i, j = 0, 0
            while i < len(s) and j < len(word):
                if (len(s) - i) < (len(word) - j):
                    break
                if s[i] == word[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            if j == len(word):
                if len(answer) < len(word):
                    answer = word
                
        return answer