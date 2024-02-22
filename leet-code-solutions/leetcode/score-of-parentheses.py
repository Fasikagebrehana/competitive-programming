class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                last = stack.pop()
                current = stack.pop()
                res = current + max(last * 2, 1)
                stack.append(res)
        return stack[len(stack) - 1]