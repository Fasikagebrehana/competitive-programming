class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [['U' for _ in range(n)] for _ in range(m)]
        for r,c in walls:
            grid[r][c] = 'W'
        for r,c in guards:
            grid[r][c] = 'W'
            
        for r, c in guards:
            for i in range(c - 1, -1, -1):
                if self.checker(r, i, grid):
                    break
                grid[r][i] = 'M'
            for i in range(c + 1, n):
                if self.checker(r, i, grid):
                    break
                grid[r][i] = 'M'
            for i in range(r - 1, -1, -1):
                if self.checker(i, c, grid):
                    break
                grid[i][c] = 'M'
            for i in range(r + 1, m):
                if self.checker(i, c, grid):
                    break
                grid[i][c] = 'M'
        
        return sum(row.count('U') for row in grid)
    
    def checker(self,r,c,grid):
            return grid[r][c] in ['W', 'G']