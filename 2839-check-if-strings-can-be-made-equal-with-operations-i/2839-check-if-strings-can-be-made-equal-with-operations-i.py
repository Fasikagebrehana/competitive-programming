class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        n, m = len(s1) //2, len(s2) //2
        if s1 == s2:
            return True
        s1 = list(s1)
        s2 = list(s2)
        for i in range(2):
            if s1[i] != s2[i]:
                s2[i], s2[i+2] = s2[i+2], s2[i]
        if s1 != s2:
            return False
        return True