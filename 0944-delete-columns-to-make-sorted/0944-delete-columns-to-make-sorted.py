class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for i in range(0, len(strs[0])):
            for j in range(1, len(strs)):
                if strs[j-1][i-1] > strs[j][i-1]:
                    count += 1
                    break
        return count