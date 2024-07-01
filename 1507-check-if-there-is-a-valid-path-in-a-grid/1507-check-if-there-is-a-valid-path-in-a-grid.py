class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions = [[(0, -1), (0, 1)], [(-1, 0), (1, 0)], [(0, -1), (1, 0)], [(0, 1), (1, 0)], [(0, -1), (-1, 0)], [(0, 1), (-1, 0)]]
        def inbound(r, c):
            return (0 <= r < len(grid) and 0 <= c < len(grid[0]))
        visited = set()
        def dfs(row, col):
            visited.add((row, col))
            if (row, col) == (len(grid) -1, len(grid[0]) - 1):
                return True
            for a, b in directions[grid[row][col] - 1]:
                newRow, newCol = row + a, col + b
                if inbound(newRow, newCol) and (newRow, newCol) not in visited:
                    for x, y in directions[grid[newRow][newCol] - 1]:
                        if (newRow + x, newCol + y) == (row, col):
                            if dfs(newRow, newCol):
                                return True
            return False
        return dfs(0, 0)