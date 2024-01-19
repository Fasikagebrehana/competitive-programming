class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefixsum = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(len(matrix)):
            for c in range((len(matrix[0]))):
                self.prefixsum[r + 1][c + 1] = (self.prefixsum[r][c + 1] + 
                                                self.prefixsum[r + 1][c] - 
                                                self.prefixsum[r][c] + 
                                                matrix[r][c])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.prefixsum[row2 + 1][col2 + 1] - 
                self.prefixsum[row2 + 1][col1] - 
                self.prefixsum[row1][col2 + 1] + 
                self.prefixsum[row1][col1])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)