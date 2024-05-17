class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        store = {}
        def dp(i, j):
            if i == (len(matrix) - 1) and 0 <= j < len(matrix):
                return matrix[i][j]
            if j < 0 or j >= len(matrix):
                return inf

            if (i, j) not in store:
                store[(i, j)] =  matrix[i][j] + min(dp(i+1, j-1), dp(i+1, j+1), dp(i+1, j))
            return store[(i, j)]

        ans = inf
        for j in range(len(matrix)):
            ans = min(ans, dp(0, j))
        return ans