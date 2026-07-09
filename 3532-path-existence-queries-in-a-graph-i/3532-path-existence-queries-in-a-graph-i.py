class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # its a sorted array create a parent array
        # using union find
        parent = {i:i for i in range(n)}
        # print(parent)
        ans = []

        size = [1 for i in range(n)]
        def find(x):
            if x == parent[x]:
                return parent[x]
            return find(parent[x])
        def union(x, y):
            parentX, parentY = find(x), find(y)
            if parentX != parentY:
                if size[parentX] >= size[parentY]:
                    parent[parentY] = parent[parentX]
                    size[parentX] += size[parentY]
                else:
                    parent[parentX] = parent[parentY]
                    size[parentY] += size[parentX]
        
        for i in range(1, n):
            if (nums[i] - nums[i-1]) <= maxDiff:
                union(i-1, i)
        # print(parent)
        
        for x, y in queries:
            if find(x) == find(y):
                ans.append(True)
            else:
                ans.append(False)
        # print(ans)
        return ans
