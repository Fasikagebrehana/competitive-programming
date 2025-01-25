class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adjList = defaultdict(list)
        indegree = [0] * n
        for x, y in edges:
            adjList[x].append(y)
            indegree[y] += 1
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        ans = [set() for _ in range(n)]
        while queue:
            node = queue.popleft()
            
            for neighbour in adjList[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
                ans[neighbour].update(ans[node])
                ans[neighbour].add(node)
        return [sorted(list(a)) for a in ans]