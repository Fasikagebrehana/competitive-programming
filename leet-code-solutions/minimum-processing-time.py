class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort()
        max_pt = 0
        i, j = 3, len(processorTime)-1
        while i < len(tasks) and j < len(processorTime):
            curr = tasks[i] + processorTime[j]
            max_pt = max(max_pt, curr)
            i += 4
            j -= 1
        return max_pt