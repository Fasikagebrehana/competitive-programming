class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        current_Updated = [intervals[0]]
        for i in range(1, len(intervals)):
            # print(current_Updated[-1][0])
            if intervals[i][0] <= current_Updated[-1][1]:
                current_Updated[-1][0] = min(intervals[i][0], current_Updated[-1][0])
                current_Updated[-1][1] = max(intervals[i][1], current_Updated[-1][1])
            else:
                current_Updated.append(intervals[i])
        
        return current_Updated