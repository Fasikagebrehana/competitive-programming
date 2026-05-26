class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # print(ord('z'))
        
        lower = set()
        upper = set()
        for ch in word:
            if 97 <= ord(ch) <= 123:
                lower.add(ch)
            else:
                upper.add(ch)
        answer = 0
        for ch in upper:
            if ch.lower() in lower:
                answer += 1
        return answer