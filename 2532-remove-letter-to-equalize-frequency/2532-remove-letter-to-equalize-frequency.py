class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = Counter(word)

        for w in word:
            counter[w] -= 1
            if counter[w] == 0:
                del counter[w]
            
            if min(counter.values()) == max(counter.values()):
                return True
            
            counter[w] += 1
        return False