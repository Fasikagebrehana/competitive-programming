class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def inbounds(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        visited = set()
        def dfs(row, col):
            visited.add((row, col))

            for x, y in directions:
                newRow, newCol = row + x, col + y
                if inbounds(newRow, newCol) and grid[newRow][newCol] == '1' and (newRow, newCol) not in visited:
                    dfs(newRow, newCol)
        NumberOfIsland = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == '1':
                    dfs(i, j)
                    visited.add((i, j))
                    NumberOfIsland += 1
        return NumberOfIsland