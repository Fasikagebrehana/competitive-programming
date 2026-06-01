class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        i = 0
        cost.sort(reverse = True)
        min_cost = 0

        while i < len(cost):
            if (i + 1) < len(cost):
                min_cost += cost[i] + cost[i +1]
                i += 3
            else:
                min_cost += cost[i]
                i += 1
        return min_cost
        