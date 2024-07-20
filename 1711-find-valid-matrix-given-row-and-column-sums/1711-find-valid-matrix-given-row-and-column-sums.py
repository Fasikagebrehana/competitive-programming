class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        ans = [[0 for i in range(len(colSum))] for j in range(len(rowSum))]
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                min_num = min(rowSum[i], colSum[j])
                ans[i][j] = min_num
                rowSum[i] -= min_num
                colSum[j] -= min_num
        return ans