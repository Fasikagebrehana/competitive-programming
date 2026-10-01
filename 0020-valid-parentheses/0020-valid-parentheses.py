class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        stack = []
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            else:
                if stack and ((stack[-1] == '(' and ch == ')') or (stack[-1] == '[' and ch == ']') or (stack[-1] == '{' and ch == '}')):
                    stack.pop()
                else:
                    return False
        return True if not stack else False