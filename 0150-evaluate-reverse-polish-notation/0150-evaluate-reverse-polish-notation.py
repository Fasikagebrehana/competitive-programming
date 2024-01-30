class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        for i in range(len(tokens)):
            if tokens[i] in operators:
                b = stack.pop()
                a = stack.pop()
                if tokens[i] == "+":
                    ans = (a) + (b)
                elif tokens[i] == "-":
                    ans = (a) - (b)
                elif tokens[i] == "*":
                    ans = (a) * (b)
                else:
                    ans = (a) / (b)
                stack.append(int(ans))
            else:
                stack.append(int(tokens[i]))
        return stack[0]