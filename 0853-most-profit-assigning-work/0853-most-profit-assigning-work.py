class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        arr = []
        for i in range(len(difficulty)):
            arr.append((difficulty[i], profit[i]))
        worker.sort()
        arr.sort()
        profit = []
        diff = []
        max_p = 0
        max_profit = []
        for d, p in arr:
            diff.append(d)
            max_p = max(max_p, p)
            max_profit.append(max_p)

        ans = 0
        for num in worker:
            idx = bisect_right(diff, num)-1
            if idx >= 0:
                ans += max_profit[idx]
        return ans