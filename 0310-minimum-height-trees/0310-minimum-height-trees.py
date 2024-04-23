class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adjList = defaultdict(list)
        for x, y in edges:
            adjList[x].append(y)
            adjList[y].append(x)

        queue = deque()
        for i in range(n):
            if len(adjList[i]) == 1:
                queue.append(i)
        
        remaining_nodes = n
        while remaining_nodes > 2:
            num_nodes = len(queue)
            remaining_nodes -= num_nodes
            for _ in range(num_nodes):
                node = queue.popleft()
                neighbor = adjList[node].pop()
                adjList[neighbor].remove(node)
                if len(adjList[neighbor]) == 1:
                    queue.append(neighbor)
        return list(queue)

        # min_height = inf
        # ans = []
        
        # for i in range(n):
        #     height = bfs(i)
        #     if height > min_height:
        #         continue
        #     if min_height > height:
        #         min_height = height
        #         ans = [i]
        #     elif height == min_height:
        #         ans.append(i)
        # return ans