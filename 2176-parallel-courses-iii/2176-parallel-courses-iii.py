class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegree = [0] * n
        adjList = defaultdict(list)

        for x, y in relations:
            indegree[y-1] += 1
            adjList[x-1].append(y-1)
        # print(adjList)

        ans = [0] * n
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
                ans[i] = time[i]
        
        
        while queue:
            node = queue.popleft()

            for neigh in adjList[node]:
                indegree[neigh] -= 1
                ans[neigh] = max(ans[neigh], time[neigh] + ans[node])
                if indegree[neigh] == 0:
                    queue.append(neigh)
        return max(ans)