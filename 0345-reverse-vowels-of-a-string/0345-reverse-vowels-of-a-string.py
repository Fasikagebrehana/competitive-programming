class Solution:
    def reverseVowels(self, s: str) -> str:
        letters = list(s)
        left = 0
        right = len(letters) - 1
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        while left < right:
            if letters[left] in vowels and letters[right] in vowels:
                letters[left], letters[right] = letters[right], letters[left]
                left += 1
                right -= 1
            elif letters[left] not in vowels and letters[right] not in vowels:
                left += 1
                right -= 1
            elif letters[left] not in vowels:
                left += 1
            elif letters[right] not in vowels:
                right -= 1
            
        return ''.join(letters)