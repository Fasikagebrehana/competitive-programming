class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adjList = defaultdict(list)

        for x, y in prerequisites:
            adjList[y].append(x)
            indegree[x] += 1
        
        queue = deque()

        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        courses = []
        while queue:
            node = queue.pop()
            courses.append(node)

            for neigh in adjList[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        return courses if len(courses) == numCourses else []