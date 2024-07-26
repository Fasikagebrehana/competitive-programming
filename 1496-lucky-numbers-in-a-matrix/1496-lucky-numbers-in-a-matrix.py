class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        mininRow = []
        maxinCol = []
        lucky = []
        for i in range(len(matrix)):
            mininRow.append(min(matrix[i]))
            maxx = 0
        
        for i in range(len(matrix[0])):
            maxx = 0
            for j in range(len(matrix)):
                maxx = max(maxx, matrix[j][i])
            maxinCol.append(maxx)
            maxx = 0
        # print(maxinCol)
        # print(mininRow, maxinCol)
        for num in mininRow:
            if num in maxinCol:
                lucky.append(num)
            
        
        return lucky