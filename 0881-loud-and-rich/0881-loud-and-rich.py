class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        adjList = defaultdict(list)
        n = len(quiet)
        larger = [0] * (n )
        for x, y in richer:
            adjList[x].append(y)
            larger[y] += 1
        # print(adjList)
        ans = [i for i in range(n)]
        queue = deque()
        # visited = set()
        for i in range(n):
            if larger[i] == 0:
                queue.append(i)
                # ans[i] = i
        # print(larger)
        minn = inf
        while queue:
            node = queue.popleft()
            for neighbour in adjList[node]:
                if quiet[ans[neighbour]] > quiet[ans[node]]:
                    ans[neighbour] = ans[node]
                else:
                    ans[neighbour] = ans[neighbour]
                larger[neighbour] -= 1
                if larger[neighbour] == 0:
                        queue.append(neighbour)
                    
        return ans