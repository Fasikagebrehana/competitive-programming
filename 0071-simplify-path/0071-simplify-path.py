class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        # checker = []
        ans = '/'
        
        path = path.split('/')
        for p in path:
            if stack and p == '..':
                stack.pop()
            elif p == '' or p == '.' or p == '..':
                continue
            else:
                stack.append(p)
        ans += '/'.join(stack)
        return ans