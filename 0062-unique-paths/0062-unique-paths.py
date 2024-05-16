class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        store = {}
        def dp(row, col):
            if row == m - 1 and col == n - 1:
                return 1
            right, down = 0, 0
            if (row, col) not in store:
                if row < m:
                    right = dp(row + 1, col)
                if col < n:
                    down = dp(row, col + 1)
                store[(row, col)] = right + down
            return store[(row, col)]
        return dp(0, 0)