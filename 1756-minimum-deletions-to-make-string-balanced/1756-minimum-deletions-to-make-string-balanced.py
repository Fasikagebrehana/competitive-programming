class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack = [s[-1]]
        count = 0
        for i in range(len(s)-2, -1, -1):
            if stack and s[i] == 'b' and stack[-1] == 'a':
                stack.pop()
                count += 1
            else:
                stack.append(s[i])
        
        return count
