class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        
        counterS = Counter(s)
        counterT = Counter(t)

        for key, val in counterT.items():
            if counterS[key] != val:
                return False
        return True