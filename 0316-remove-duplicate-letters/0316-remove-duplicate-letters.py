class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        last_occur = {}
        for i in range(len(s)):
            last_occur[s[i]] = i
        print(last_occur)
        seen = set()

        for i in range(len(s)):
            if s[i] not in seen:
                while stack and s[i] < stack[-1] and last_occur[stack[-1]] > i:
                    temp = stack.pop()
                    seen.remove(temp)
                
                stack.append(s[i])
                seen.add(s[i])

        return ''.join(stack)