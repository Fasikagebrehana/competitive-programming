class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        a = ord('a')
        parent = {chr(a): chr(a) for a in range(ord('a'), ord('z') + 1)}
        
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parentX = find(x)
            parentY = find(y)
            if parentX != parentY:
                if ord(parentX) <= ord(parentY):
                    parent[parentY] = parentX
                else:
                    parent[parentX] = parentY

        for i in range(len(s1)):
            union(s1[i], s2[i])
        print(parent)

        ans = ""
        for s in baseStr:
            ans += find(s)
        return ans