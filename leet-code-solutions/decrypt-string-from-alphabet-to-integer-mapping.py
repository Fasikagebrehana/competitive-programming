class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabet = {}
        for u, val in enumerate(range(ord('a'), ord('i') + 1), start = 1 ):
            alphabet[str(u)] = chr(val)
        for a, val in enumerate(range(ord('j'), ord('z') + 1), start = 10):
            alphabet[str(a) + '#'] = chr(val)
            
        ans = []
        i = 0
        while i < len(s):
            if i+2 < len(s) and s[i+2] == '#':
                ans.append(alphabet[s[i:i+3]])
                i += 3
            else:
                ans.append(alphabet[s[i]])
                i += 1
        return ''.join(ans)