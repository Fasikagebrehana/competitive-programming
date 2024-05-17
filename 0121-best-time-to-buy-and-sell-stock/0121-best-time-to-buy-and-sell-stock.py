class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        store = {}
        n = len(prices)
        def profit(i, state):
            if i  >= n:
                return 0
            if (i, state) not in store:
                if not state:
                    store[((i, state))] = max(profit(i + 1, not state) - prices[i], profit(i+1, state))
                else:
                    store[((i, state))] = max(prices[i], profit(i+1, state))
            return store[(i, state)]
        return profit(0, False)