class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {i: i for i in range(26)}
        size = [1] * (26)
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            parentX, parentY = find(x), find(y)

            if parentX != parentY:
                if parentX <= parentY:
                    parent[parentY] = parentX
                    size[parentX] += size[parentY]
                else:
                    parent[parentX] = parentY
                    size[parentY] += size[parentX]

        for i in range(len(s1)):
            a = ord(s1[i]) - ord('a')
            # print(ord(s1[i]), ord('a'))
            # print(a)
            b = ord(s2[i]) - ord('a')
            union(a, b)
        # print(parent)
        answer = []
        for s in baseStr:
            p = ord(s) - ord('a')
            # print(p)
            ch = find(p)
            # print(ch)
            ch += ord('a')
            answer.append(chr(ch))
        return ''.join(answer)