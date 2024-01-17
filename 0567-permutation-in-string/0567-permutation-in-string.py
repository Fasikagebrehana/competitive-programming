class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = len(s1)
        count_s1 = Counter(s1)
        for right in range(len(s2)):
            if Counter(s2[right: right + a]) == count_s1:
                return True
        return False