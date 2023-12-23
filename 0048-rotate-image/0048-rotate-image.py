class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(len(matrix)):
            n = 0
            m = len(matrix) -1
            while n <= m:
                matrix[i][n], matrix[i][m] = matrix[i][m], matrix[i][n]
                n += 1
                m -= 1
                