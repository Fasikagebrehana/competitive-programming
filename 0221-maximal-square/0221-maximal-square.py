class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix[0])
        m = len(matrix)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        ans = 0
        for i in range(m-1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    dp[i][j] = int(matrix[i][j]) + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
                    ans = max(ans, dp[i][j])
        return ans * ans
