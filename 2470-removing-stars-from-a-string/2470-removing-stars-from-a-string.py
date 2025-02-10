class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i].isalpha():
                stack.append(s[i])
            else:
                if stack and stack[-1].isalpha():
                    stack.pop()
        return ''.join(stack)