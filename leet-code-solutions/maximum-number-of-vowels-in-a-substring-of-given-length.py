class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l, r = 0, k
        vowel_count = 0
        vowel = {'a': 1, 'e': 2, 'i':3, 'o':4, 'u':5}
        for i in range(k):
            if s[i] in vowel:
                vowel_count += 1
        max_vowel_count = vowel_count
        while r < len(s):
            if s[r] in vowel:
                vowel_count += 1
            if s[l] in vowel:
                vowel_count -= 1
            l += 1
            r += 1
            max_vowel_count = max(max_vowel_count, vowel_count)
        return max_vowel_count