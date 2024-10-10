class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        
        for x, y, w in flights:
            graph[x].append((y, w))
        
        prev = [inf] * n
        prev[src] = 0
        # print(prev)
        for i in range(k+1):
            curr = prev[:]

            for u, v, w in flights:
                curr[v] = min(curr[v], prev[u] + w)
        
            prev = curr[:]
        
        return curr[dst] if curr[dst] != inf else -1