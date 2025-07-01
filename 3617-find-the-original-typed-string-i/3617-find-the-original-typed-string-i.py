class Solution:
    def possibleStringCount(self, word: str) -> int:
        left  = total= 0
        if len(word) == 1:
            return 1
        for i in range(len(word)-1):
            if word[i] != word[i+1]:
                total += (i- left)
                left = i+ 1
        # print(total)
        # print(i, left)
        if word[left] == word[i]:
            total += (i+1 - (left))
        
        # print(total)
        return total + 1