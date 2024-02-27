class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]
        def pascal(idx):
            if idx == 0:
                return [1]
            if idx == 1:
                return [1,1]
            curr = []
            prev = pascal(idx-1)
            for i in range(1,len(prev)):
                curr.append(prev[i] + prev[i-1])
            return [1] + curr + [1]
        return pascal(rowIndex)