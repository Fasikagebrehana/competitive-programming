class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        task = sorted(tasks, key=lambda tasks:(tasks[1] - tasks[0]), reverse=True)
        ans = task[0][1]
        curr_min = task[0][1]
        
        for actual, minimum in task:
            if curr_min >= minimum:
                curr_min -= actual
            else:
                ans += (minimum - curr_min)
                curr_min += (minimum - curr_min)
                curr_min -= actual
        return ans