class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        for x, y in prerequisites:
            indegree[x] += 1
        
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        adjList = defaultdict(list)
        for x, y in prerequisites:
            adjList[y].append(x)
        count = 0
        while queue:
            node = queue.popleft()
            count += 1

            for neigh in adjList[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
            if count == numCourses:
                return True
        return False
            