class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        store = []
        idx = 0
        for i in range(len(s)):
            if idx < len(spaces) and i == spaces[idx]:
                store.append(' ')
                idx += 1
            store.append(s[i])
        
        return ''.join(store)