class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        idx = word.index(ch)
        ans = ""
        ans += word[:idx+1][::-1]
        ans += word[idx+1:]
        return ans