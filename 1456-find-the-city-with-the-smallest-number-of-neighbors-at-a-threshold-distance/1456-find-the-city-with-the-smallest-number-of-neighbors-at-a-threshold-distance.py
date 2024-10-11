class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distances= [[inf] * n for _ in range(n)]

        for v, u, w in edges:
            distances[u][v] = distances[v][u] = w

        for i in range(n):
            distances[i][i] = 0
        # print(distancestances)

        for inter in range(n):
            for i in range(n):
                for j in range(n):
                    if distances[i][j] > (distances[i][inter] + distances[inter][j]):
                        distances[i][j] = (distances[i][inter] + distances[inter][j])
        c = inf
        ans = 0
        # print(distances)
        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and distances[i][j] <= distanceThreshold:
                    count += 1
            if count <= c:
                c = count
                ans = i
        return ans