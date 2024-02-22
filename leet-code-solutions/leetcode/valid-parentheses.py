class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')':'(', ']':'[', '}':'{'}
        for c in s:
            
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                top = stack.pop() if stack else '0'
                if top != dic[c]:
                    return False
        if len(stack) == 0:
            return True
        else:
            False