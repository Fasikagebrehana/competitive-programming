class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cost = sorted(costs, key=lambda costs:(costs[0]-costs[1]))
        n = len(costs)//2
        ans = 0
        for i in range(n):
            ans += cost[i][0] + cost[i+n][1]
        return ans