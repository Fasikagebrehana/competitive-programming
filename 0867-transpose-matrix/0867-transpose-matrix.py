class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row, col = len(matrix), len(matrix[0])
        ans = [[0] * row for _ in range(col)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                ans[j][i] = matrix[i][j]
        return ans