class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        adjList = defaultdict(list)
        for i in range(n-1):
            adjList[i].append(i+1)
        # print(adjList)

        def shortestPath():
            heap = [(0, 0)]
            visited = set()
            while heap:
                length, node = heappop(heap)
                if node in visited:
                    continue
                if node == (n - 1):
                    return length
                visited.add(node)
                for neigh in adjList[node]:
                    if neigh not in visited:
                        heappush(heap, (length + 1, neigh))


        answer = []
        for x, y in queries:
            adjList[x].append(y)
            answer.append(shortestPath())

        return answer