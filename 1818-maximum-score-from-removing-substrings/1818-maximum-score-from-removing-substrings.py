class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # stack
        maxPoints = 0
            
        def helper(s, first, second, xORy):
            stack = []
            currMax = 0
            for i in range(len(s)):
                if not stack:
                    stack.append(s[i])
                elif stack[-1] == first and s[i] == second:
                    currMax += xORy
                    stack.pop()
                else:
                    stack.append(s[i])
            return stack, currMax
        
        if x > y:
            remainderLetters, currentMaxFirst = helper(s, 'a', 'b', x)
            remainderLetters, currentMaxSecond = helper(remainderLetters, 'b', 'a', y)
        else:
            remainderLetters, currentMaxFirst = helper(s, 'b', 'a', y)
            remainderLetters, currentMaxSecond = helper(remainderLetters, 'a', 'b', x)
        # print(currentMaxFirst, currentMaxSecond)

        return currentMaxFirst + currentMaxSecond