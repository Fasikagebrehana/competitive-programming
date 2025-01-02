class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a', 'e', 'i', 'o', 'u']
        prefix = [0] * len(words)
        if words[0][0] in vowels and words[0][-1] in vowels:
            prefix[0] = 1
        for i in range(1, len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix[i] = prefix[i-1] + 1
            else:
                prefix[i] = prefix[i-1]
        # print(prefix)
        answer = []
        for l, r in queries:
            if l == 0:
                answer.append(prefix[r])
            else:
                answer.append(prefix[r] - prefix[l-1])
        return answer