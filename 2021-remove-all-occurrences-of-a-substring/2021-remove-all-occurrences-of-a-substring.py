class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        last = part[-1]
        m = len(part)
        for i in range(len(s)):
            stack.append(s[i])
            if stack[-1] == last:
                if len(stack) >= m:
                    # print(stack[-1])
                    # print(stack[i - m + 1: i+1])
                    if ''.join(stack[len(stack) - m: len(stack) +1]) == part:
                        k = m
                        while k > 0:
                            stack.pop()
                            k -= 1
        return ''.join(stack)