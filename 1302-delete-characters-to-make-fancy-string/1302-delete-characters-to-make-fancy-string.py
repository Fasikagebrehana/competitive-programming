class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = [s[0]]
        for i in range(1, len(s)):
            if len(stack) >= 2 and s[i] == stack[-1] == stack[-2]:
                continue
            else:
                stack.append(s[i])
        # print(stack)
        return ''.join(stack)