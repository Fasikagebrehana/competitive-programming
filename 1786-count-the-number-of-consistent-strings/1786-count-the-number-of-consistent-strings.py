class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed =set(allowed)
        count = 0

        for word in words:
            flag = True
            for letter in word:
                if letter not in allowed:
                    flag = False

            if flag:
                count += 1
        
        return count