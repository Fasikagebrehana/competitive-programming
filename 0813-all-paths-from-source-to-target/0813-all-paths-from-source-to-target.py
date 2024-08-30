class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        arr = []
        ans = []
        visited = set()

        n = len(graph)
        def dfs(node):
            nonlocal arr
            arr.append(node)
            for neigh in graph[node]:
                dfs(neigh)
            if node == n - 1:
                ans.append(arr.copy())
            
            arr.pop()

        
        dfs(0)
        return ans