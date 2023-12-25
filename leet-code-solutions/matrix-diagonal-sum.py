class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        i = 0
        dsum = 0
        n = len(mat)
        while i < n:
            dsum += mat[i][i]
            dsum += mat[i][n-1-i]
            if i == (n-1-i):
                dsum -= mat[i][i]
            i += 1
            
        return dsum
            