class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        counter1 = Counter(s1)
        counter2 = Counter(s2)
        different = 0
        for i in range(len(s1)):
            if counter1[s1[i]] != counter2[s1[i]]:
                return False
            if s1[i] != s2[i]:
                different += 1
            if different > 2:
                return False
        return True