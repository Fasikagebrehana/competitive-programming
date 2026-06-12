class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        max_depth = 0
        mod = 10**9 + 7
        # construct the graph
        adjList = defaultdict(list)
        for x, y in edges:
            adjList[x].append(y)
            adjList[y].append(x)
        visited = set()
        
        # for i in range(1, len(edges)+ 1):

        def dfs(node, depth):
            max_depth = depth
            for neigh in adjList[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    max_depth = max(max_depth, dfs(neigh, depth + 1))
                
            return max_depth
        visited.add(1)
        depth = dfs(1, 0)
        # after getting the max depth we just need to know the count of odd since they're the factoring that matters in parity
        return pow(2, depth - 1, mod)