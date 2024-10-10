class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # create distances dic 
        # create the graph
        # I'm gonna return th max distance from all distances
        distances = {i : inf for i in range(1, n+1)}
        # print(distances)
        distances[k] = 0
        visited = set()
        graph = defaultdict(list)
        for x, y, w in times:
            graph[x].append((w, y))
        # print(graph)
        heap = [(0, k)]
        while heap:
            weight, node = heappop(heap)
            visited.add(node)
            for w, neigh in graph[node]:
                if neigh in visited:
                    continue
                dis = weight + w
                if dis < distances[neigh]:
                    distances[neigh] = dis
                    heappush(heap, (dis, neigh))
        ans = 0
        for key, val in distances.items():
            ans = max(ans, val)

        return ans if ans != inf else -1
