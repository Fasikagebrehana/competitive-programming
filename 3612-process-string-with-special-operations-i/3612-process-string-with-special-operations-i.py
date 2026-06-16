class Solution:
    def processStr(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch.isalpha():
                stack.append(ch)
            elif ch == '*':
                if stack:
                    stack.pop()
            elif ch == '#':
                stack += stack[:]
            else:
                stack = stack[::-1]
        
        return ''.join(stack)