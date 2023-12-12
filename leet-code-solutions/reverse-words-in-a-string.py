class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        w = word[::-1]
        return ' '.join(w)
        