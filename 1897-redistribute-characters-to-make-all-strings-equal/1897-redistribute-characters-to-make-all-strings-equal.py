class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        dic = {}
        if len(words) == 1:
            return True
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j] not in dic:
                    dic[words[i][j]] = 1
                else:
                    dic[words[i][j]] += 1
        for letter in dic:
            if dic[letter] % len(words) != 0:
                return False
        return True