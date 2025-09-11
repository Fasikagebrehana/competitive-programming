class Solution:
    def sortVowels(self, s: str) -> str:
        all_vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u','U'}
        vowels = []
        for ss in s:
            if ss in all_vowels:
                vowels.append(ss)
        vowels.sort()
        # print(vowels)

        idx = 0
        answer = []
        for i in range(len(s)):
            if s[i] in all_vowels:
                answer.append(vowels[idx])
                idx += 1
            else:
                answer.append(s[i])
        return ''.join(answer)