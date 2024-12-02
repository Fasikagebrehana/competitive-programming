class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = [intervals[0]]
        # print(answer)
        for i in range(1, len(intervals)):
            
            if intervals[i][0] <= answer[-1][1]:
                answer[-1][1] = max(intervals[i][1], answer[-1][1])
            else:
                answer.append(intervals[i])
        return answer
            
        