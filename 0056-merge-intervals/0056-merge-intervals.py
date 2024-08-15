class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        print(intervals)
        ans = []
        if len(intervals) == 1:
            ans.append([intervals[0][0], intervals[0][1]])
            return ans

        ans.append([intervals[0][0], intervals[0][1]])

        for i in range(1, len(intervals)):
            if ans[-1][1] >= intervals[i][0]:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                ans.append([intervals[i][0], intervals[i][1]])
                

        return ans