class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel_max = max(s.count('a'), s.count('e'), s.count('i'), s.count('o'), s.count('u'))
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        
        counter = defaultdict(int)
        for l in s:
            if l not in vowels:
                counter[l] += 1
        consonant_max = max(counter.values()) if counter else 0
        return vowel_max + consonant_max