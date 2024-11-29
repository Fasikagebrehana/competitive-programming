class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        heap = [(0, 0, 0)]

        directions = [(0, 1), (-1, 0), (1, 0), (0, -1)]

        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1        

        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        visited = set()
        
        while heap:
            time, row, col = heappop(heap)
            if row == (len(grid) - 1) and col == (len(grid[0]) - 1):
                return time
            if (row, col) in visited:
                continue
            visited.add((row, col))

            for x, y in directions:
                newRow, newCol = row + x, col + y
                if inbound(newRow, newCol) and (newRow, newCol) not in visited:
                    if (time + 1) >= grid[newRow][newCol]:
                        heappush(heap, (time + 1, newRow, newCol))
                    else:
                        # finding the time to move to the grid[newRow][newCol]
                        remainder = grid[newRow][newCol] - time
                        if remainder % 2 == 0:
                            heappush(heap, (grid[newRow][newCol] + 1, newRow, newCol))
                        else:
                            heappush(heap, (grid[newRow][newCol], newRow, newCol))
        return -1