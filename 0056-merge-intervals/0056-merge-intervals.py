class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        if len(intervals) == 1:
            ans.append([intervals[0][0], intervals[0][1]])
            return ans

        for i in range(1, len(intervals)):
            if intervals[i][0] <= intervals[i-1][1]:
                ans.append([intervals[i-1][0], intervals[i][1]])
            else:
                ans.append([intervals[i][0], intervals[i][1]])
        return ans