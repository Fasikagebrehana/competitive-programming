class Solution:
    def isCircularSentence(self, s: str) -> bool:
        words = s.split()
        for i in range(1, len(words)):
            if words[i-1][-1] != words[i][0]:
                return False
        if words[0][0] != words[-1][-1]:
            return False
        return True