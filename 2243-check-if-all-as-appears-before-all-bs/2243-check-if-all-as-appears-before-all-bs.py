class Solution:
    def checkString(self, s: str) -> bool:
        stack = [s[0]]
        for i in range(1, len(s)):
            if stack and stack[-1] == 'b' and s[i] == 'a':
                return False
            else:
                stack.append(s[i])
        return True
        