class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        suffix = [0] * len(prices)
        curr = 0
        for i in range(len(prices)-1, -1, -1):
            curr = max(curr, prices[i])
            suffix[i] = curr
        
        # print(suffix)

        for i in range(len(prices)):
            profit = max(profit, suffix[i] - prices[i])

        return profit