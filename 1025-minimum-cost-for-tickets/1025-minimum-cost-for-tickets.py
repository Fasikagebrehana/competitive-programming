class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        store ={}
        def dp(idx):
            if idx >= len(days):
                return 0
            if idx not in store:
                one = costs[0] + dp(idx + 1)
                seven = costs[1] + dp((bisect_left(days, days[idx] + 7)))
                thirty = costs[2] + dp((bisect_left(days, days[idx] + 30)))
                store[idx] = min(one, seven, thirty)
            return store[idx]

        return dp(0)