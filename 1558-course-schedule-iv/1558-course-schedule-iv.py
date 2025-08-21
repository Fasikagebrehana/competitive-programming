class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        indegree = [0] * (numCourses)
        # check if x is a prerequisite of y, we have to save the prerequisites of each 
        store = defaultdict(set)
        adjList = defaultdict(list)
        for i in range(len(prerequisites)):
            x, y = prerequisites[i]
            indegree[y] += 1
            adjList[x].append(y)

        # print(indegree)
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        # print(queue)

        while queue:
            node = queue.popleft()

            for neigh in adjList[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
                # since we also need the prerequisites of the previous node we need to add it to our store by using update method 
                store[neigh].add(node)
                store[neigh].update(store[node])
        # print(store)
        answer = []
        for x, y in queries:
            if x in store[y]:
                answer.append(True)
            else:
                answer.append(False)
        # print(answer)
        return answer