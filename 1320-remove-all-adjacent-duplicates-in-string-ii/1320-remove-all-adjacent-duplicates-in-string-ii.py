class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        count = 0
        stack = []
        # stack.append(s[0])
        i = 0
        while i < len(s):
            if stack and stack[-1][0] == s[i]:
                stack[-1][1] += 1
            else:
                stack.append([s[i], 1])
            
            if stack[-1][1] == k:
                stack.pop()
            i += 1
        
        ans = ''.join(ch * count for ch, count in stack)
        return ans