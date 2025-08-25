class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        store = {}
        def dp(i, j):
            if i == len(grid) or j == len(grid[0]):
                return inf
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return grid[i][j]
            if (i, j) not in store:
                store[(i, j)] = grid[i][j] + min(dp(i, j+1), dp(i+1, j))
            return store[(i, j)]
        return dp(0,0)
