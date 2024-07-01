class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions = {1: [(0, -1), (0, 1)], 2: [(-1, 0), (1, 0)], 3: [(0, -1), (1, 0)], 4: [(0, 1), (1, 0)], 5: [(0, -1), (-1, 0)], 6: [(0, 1), (-1, 0)]}
        def inbound(r, c):
            return (0 <= r < len(grid) and 0 <= c < len(grid[0]))
        visited = set()
        def dfs(row, col):
            visited.add((row, col))
            if (row, col) == (len(grid) - 1, len(grid[0]) - 1):
                return True
            
            for x, y in directions[grid[row][col]]:
                if inbound(x + row, y + col) and (-x, -y) in directions[grid[row + x][col + y]] and (x + row, y + col) not in visited:
                    if dfs(x + row, y + col):
                        return True
            return False
        return dfs(0, 0)