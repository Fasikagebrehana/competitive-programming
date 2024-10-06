class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()

        l1, l2 = 0, 0
        r1, r2 = len(s1), len(s2)
        
        prefix, suffix = 0, 0
        while l1 < r1 and l2 < r2 and s1[l1] == s2[l2]:
            prefix += 1
            l1 += 1
            l2 += 1
        
        while r1 > 0 and r2 > 0 and s1[r1 - 1] == s2[r2 - 1]:
            suffix += 1
            r1 -= 1
            r2 -= 1
        
        return prefix + suffix >= min(len(s1), len(s2))