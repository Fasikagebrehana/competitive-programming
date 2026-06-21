class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        max_bars = 0
        count = 0
        for i in range(len(costs)):
            if (costs[i] + max_bars) <= coins:
                max_bars += costs[i]
                count += 1
        
        return count