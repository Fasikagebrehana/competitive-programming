class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # count of negative numbers matter if its odd, one smaller number will not be added else all will be added
        # but if there is zero, it can neutralize
        total = 0
        negative, zeros = 0, 0
        zero = matrix.count(0)
        # print(zeros)
        minn = inf

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                total += abs(matrix[i][j])

                if matrix[i][j] < 0:
                    negative += 1
                minn = min(minn, abs(matrix[i][j]))
        
        if (negative) > 0:
            if ((negative) % 2 != 0 and zero <= 0):
                # total = total
                total = (total - minn) - minn
            # else:
                            
        # print(total)
        return total