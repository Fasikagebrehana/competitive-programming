class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        distances = [inf for _ in range(n)]
        # queue = deque([start_node])
        distances[start_node] = 0

        graph = defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], (succProb[i])))
            graph[edges[i][1]].append((edges[i][0], (succProb[i])))
        # print(graph)

        heap = [(-1, start_node)]
        processed = set()

        while heap:
            weight, node = heappop(heap)
            if node in processed:
                continue
            processed.add(node)

            for neigh, w in graph[node]:
                # if neigh in processed:
                #     continue
                dis = weight * w
                if distances[neigh] > dis:
                    distances[neigh] = dis
                    # print(dis)
                    heappush(heap, (dis, neigh))
        
        return -(distances[end_node]) if distances[end_node] != inf else 0