class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        n = len(meetings)
        
        meetings.sort()
        no_meeting = 0

        merged = [meetings[0]]
        for i in range(1, n):
            if merged[-1][1] >= meetings[i][0]:
                merged[-1][1] = max(merged[-1][1], meetings[i][1])
            else:
                merged.append(meetings[i])
        # print(merged)

        for i in range(len(merged) - 1):
            no_meeting += (merged[i+1][0] - merged[i][1] - 1)
        
        if merged[0][0] > 1:
            no_meeting += merged[0][0] - 1
        if merged[-1][1] < days:
            no_meeting += (days - merged[-1][1])

        return no_meeting