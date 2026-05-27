class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # you can also first track the smallest index of the upercases in hashmap since the length are 26 max
        # then for each upercase you can look for if there is any lowercase before it and after it
        wordSet = set(word)
        dic = {}
        special = 0
        for i, char in enumerate(word):
            if char.isupper() and char.lower() in wordSet:
                if char not in dic:
                    dic[char] = i
        
        for i, char in enumerate(word):
            if char.islower() and char.upper() in dic:
                if i > dic[char.upper()]:
                    dic.pop(char.upper())
        
        return len(dic)
        