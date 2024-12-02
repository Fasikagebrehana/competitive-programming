class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        for i in range(len(words)):
            l, r = 0, 0
            while l < len(words[i]) and r < len(searchWord):
                if words[i][l] != searchWord[r]:
                    break
                l += 1
                r += 1
            if r >= len(searchWord):
                return (i+1)
        return -1