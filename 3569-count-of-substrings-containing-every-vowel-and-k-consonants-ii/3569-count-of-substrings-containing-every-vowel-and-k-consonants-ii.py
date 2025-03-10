class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        counter = defaultdict(int)
        consonant = 0
        total_substring = 0
        right = left = 0
        while right < len(word):
            if word[right] in vowels:
                counter[word[right]] += 1
            else:
                consonant += 1
            
            while left < right and len(counter) == 5 and consonant >= k:
                total_substring += len(word) - right
                
                if word[left] in vowels:
                    counter[word[left]] -= 1
                    if counter[word[left]] == 0:
                        del counter[word[left]]
                else:
                    consonant -= 1
                left += 1
            right += 1

        counter = defaultdict(int)
        consonant = 0
        total_substring2 = 0
        right = left = 0
        while right < len(word):
            if word[right] in vowels:
                counter[word[right]] += 1
            else:
                consonant += 1
            
            while left < right and len(counter) == 5 and consonant >= (k+1):
                total_substring2 += len(word) - right
                
                if word[left] in vowels:
                    counter[word[left]] -= 1
                    if counter[word[left]] == 0:
                        del counter[word[left]]
                else:
                    consonant -= 1
                left += 1
            right += 1

        # print(total_substring)
        return total_substring - total_substring2