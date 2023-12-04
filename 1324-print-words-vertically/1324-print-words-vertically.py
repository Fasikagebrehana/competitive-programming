class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(' ')
        ans = []
        maxim = max(len(word) for word in words)
        for i in range(maxim):
            letters = []
            for word in words:
                letters.append(word[i] if i < len(word) else ' ')
            ans.append(''.join(letters).rstrip())
        return ans
    