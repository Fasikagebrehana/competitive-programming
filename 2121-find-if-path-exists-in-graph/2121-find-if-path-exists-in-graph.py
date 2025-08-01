class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        # build the graph
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        # use a bfs starting from the source then try ro find the destination
        queue = deque([source])
        visited = set({source})
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            
            for neigh in graph[node]:
                if neigh == destination:
                    return True
                if neigh not in visited:
                    visited.add(neigh)
                    queue.append(neigh)
        return False