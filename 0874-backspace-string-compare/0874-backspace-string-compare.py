class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        idx = 0
        stackS = []
        while idx < len(s):
            if s[idx] == '#':
                if stackS:
                    stackS.pop()
            else:
                stackS.append(s[idx])
            idx += 1
        
        i = 0
        stackT = []
        while i < len(t):
            if t[i] == '#':
                if stackT:
                    stackT.pop()
            else:
                stackT.append(t[i])
            i += 1
        return ''.join(stackS) == ''.join(stackT)
            