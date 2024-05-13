class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            if grid[i][0] == 0:
                for j in range(len(grid[i])):
                    grid[i][j] = 1 - grid[i][j]

        for i in range(len(grid[0])):
            zero, one = 0, 0
            for j in range(len(grid)):
                if grid[j][i] == 0:
                    zero += 1
                else:
                    one += 1
            if zero > one:
                for j in range(len(grid)):
                    grid[j][i] = 1 - grid[j][i]
        ans = 0
        for i in range(len(grid)):
            ans += int("".join(map(str, grid[i])), 2)
        return ans