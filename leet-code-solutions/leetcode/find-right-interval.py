class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # if len(intervals) == 1:
        #     return [-1]
        ans = []
        indices = []
        start = []
        comb = []
        for i in range(len(intervals)):
            comb.append((intervals[i][0], i))
        comb.sort()
        for s, j in comb:
            start.append(s)
            indices.append(j)
        for s, end in intervals:
            temp = bisect_left(start, end)
            if temp >= len(intervals):
                ans.append(-1)
            else:
                ans.append(indices[(temp)])
        return ans