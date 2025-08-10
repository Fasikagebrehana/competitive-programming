class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        # the plan: use bfs/dfs traverse starting from the firs rotten orange then change their neighbours if they are fresh oranges
        visited = set()
        # def dfs(r, c, count):
        #     if r == len(grid) and c == len(grid[0]) - 1:
        #         return count
            
        #     for x, y in directions:
        #         nextRow, nextCol = r + x, c + y
        #         if inbound(nextRow, nextCol) and (nextRow, nextCol) not in visited and grid[nextRow][nextCol] != 0:
        #             visited.add(nextRow, nextCol)
        #             if grid[nextRow][nextCol] == 1:
        #                 grid[nextRow][nextCol] = 2
        count = 0
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j ) not in visited and grid[i][j] == 2:
                    queue.append((i, j, count))
        while queue:
            # if r == len(grid) and c == len(grid[0]) - 1:
            #     return count
            r,c, count = queue.popleft()
            for x, y in directions:
                nextRow, nextCol = r + x, c + y
                if inbound(nextRow, nextCol) and (nextRow, nextCol) not in visited and grid[nextRow][nextCol] != 0:
                    visited.add((nextRow, nextCol))
                    if grid[nextRow][nextCol] == 1:
                        grid[nextRow][nextCol] = 2
                        queue.append((nextRow, nextCol, count + 1))
                    
        # print(count)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return count