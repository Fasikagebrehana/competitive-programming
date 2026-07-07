class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # sort ascending order but if they have same start sort them in descending order by making them -ve
        intervals = sorted(intervals, key=lambda x:(x[0], -x[1]))
        # print(intervals)
        count = 1
        x, y = intervals[0]
        
        for i in range(1, len(intervals)):
            if intervals[i][1] <= y:
                continue
            else:
                count += 1
                x, y = intervals[i]
        return count