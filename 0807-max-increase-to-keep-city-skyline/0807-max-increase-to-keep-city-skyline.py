class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        totalSum = 0
        for i in range(len(grid)):
            mininRow = max(grid[i])
            for j in range(len(grid[0])):
                maxCol = max(row[j] for row in grid)
                minRowCol = min(mininRow, maxCol)
                totalSum += (minRowCol - grid[i][j])
        return totalSum