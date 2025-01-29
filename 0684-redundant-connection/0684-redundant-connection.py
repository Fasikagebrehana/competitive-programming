class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {i: i for i in range(1, len(edges) + 1)}
        # print(parent)

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            parentX, parentY = find(x), find(y)
            
            if parentX != parentY:
                parent[parentY] = parentX
                return True
            else:
                return False
        answer = []
        for x, y in edges:
            if not union(x, y):
                answer.append(x)
                answer.append(y)
        return answer