class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        flag = True
        if len(matrix) < 2:
            return True
        else:
            for i in range(len(matrix)-1):
                j = 0
                while j < len(matrix[0])-1:
                    if matrix[i][j] != matrix[i+1][j+1]:
                        flag = False
                        break
                    else:
                        # i += 1
                        j += 1
            return flag