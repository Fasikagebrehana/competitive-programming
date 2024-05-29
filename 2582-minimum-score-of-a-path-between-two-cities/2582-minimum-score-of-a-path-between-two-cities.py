class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = {i: i for i in range(1, n+1)}
        size = [1] * (n+1)
        minDis = [inf for i in range(n+1)]
        def find(x):
            if x == parent[x]:
                return parent[x]
            parent[x] = find(parent[x])
            return parent[x]


        def union(x, y, dis):
            parentX = find(x)
            parentY = find(y)
            # minDis[parentY] = min(dis, minDis[parentX], minDis[parentY])
            if parentY != parentX:
                if size[parentY] > size[parentX]:
                    parent[parentX] = parentY
                    size[parentX] += size[parentX]
                else:
                    parent[parentY] = parentX
                    size[parentY] += size[parentX]
                minDis[parentX] = min(dis, minDis[parentX], minDis[parentY])
                minDis[parentY] = min(dis, minDis[parentX], minDis[parentY])
            else:
                minDis[parentY] = min(dis, minDis[parentY])
                minDis[parentX] = min(dis, minDis[parentX])

        for a, b, distance in roads:
            union(a, b, distance)
        root1 = find(1)
        return minDis[root1]