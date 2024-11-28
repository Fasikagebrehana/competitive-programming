class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        heap = [(0, 0, 0)]
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        def inbounds(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        count = 0
        visited = set((0, 0))
        while heap:
            c, row, col = heappop(heap)
            # print((row, col))
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return c
            for x, y in directions:
                newRow, newCol = row + x, col + y
                if inbounds(newRow, newCol) and (newRow, newCol) not in visited:
                    heappush(heap, (c + grid[newRow][newCol], newRow, newCol))
                    visited.add((newRow, newCol))
        return count