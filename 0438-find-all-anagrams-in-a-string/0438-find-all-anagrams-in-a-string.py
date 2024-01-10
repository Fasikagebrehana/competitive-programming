class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        target = Counter(p)
        anagram = Counter(s[:n])
        c = []
        for i in range(n, len(s)):
            if anagram == target:
                c.append(i-n)
            anagram[s[i]] += 1
            anagram[s[i-n]] -= 1
            if anagram[s[i-n]] == 0:
                del anagram[s[i-n]]
        if anagram == target:
                c.append(len(s)-n)
        return c