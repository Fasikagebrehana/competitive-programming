class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        visited = set()
        n = len(matrix)
        m = len(matrix[0])
        count = 1

        def inbound(r, c):
            return 0 <= r < n and 0 <= c < m

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            val = matrix[r][c]
            if (r, c) in memo:
                return memo[(r, c)]
            value = 0
            for x, y in directions:
                next_row, next_col = r + x, c + y
                if inbound(next_row, next_col) and matrix[next_row][next_col] > val and (next_row, next_col) not in visited:

                    value = max(dfs(next_row, next_col), value)
            memo[(r, c)] = 1 + value
            return memo[(r, c)]




        longest_increasing_path = 1
        for i in range(n):
            for j in range(m):
                visited = set()
                visited.add((i, j))
                longest_increasing_path = max(dfs(i, j), longest_increasing_path)
        
        return longest_increasing_path