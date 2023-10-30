class Solution:
    def reverseWords(self, s: str) -> str:
        w = s.split()
        reverse = [word[::-1] for word in w]
        reverse_word = ' '.join(reverse)
        return reverse_word