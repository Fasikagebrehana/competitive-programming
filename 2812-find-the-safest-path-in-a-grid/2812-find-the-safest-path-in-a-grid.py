class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def inbounds(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        
        distance = [[-1] * len(grid[0]) for _ in range(len(grid))]
        # print(distance)
        visited = set()
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    distance[i][j] = 0
        
        while queue:
            r, c = queue.popleft()

            for x, y in directions:
                newRow, newCol = x + r, y + c
                if inbounds(newRow, newCol) and distance[newRow][newCol] == -1:
                    distance[newRow][newCol] = distance[r][c] + 1
                    queue.append((newRow, newCol))
                    # visited.add((newRow, newCol))
        # print(distance)
        heap = [(-distance[0][0], 0, 0)]
       
        min_distance = inf

        while heap:
            dis, r, c = heappop(heap)
            if (r, c) == (len(grid)-1, len(grid[0])-1):
                return -dis
            safe = -(dis)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            for x, y in directions:
                nr, nc = x + r, y + c
                if inbounds(nr, nc) and (nr,nc) not in visited:
                    new_safe = min(safe, distance[nr][nc])
                    heappush(heap, (-new_safe, nr, nc))













