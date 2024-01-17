class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = len(s1)
        s1_sorted = sorted(s1)
        for right in range(len(s2)):
            if sorted(s2[right: right + a]) == s1_sorted:
                return True
        return False