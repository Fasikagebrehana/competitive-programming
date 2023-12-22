class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum = 0
        for i in range(len(grid)-2):
            curr_sum = 0
            for j in range(len(grid[0])-2):
                curr_sum = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                max_sum = max(max_sum, curr_sum)
        
        return max_sum
                