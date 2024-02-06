class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sorted_piles = sorted(piles)
        total_coins = 0
        n = len(sorted_piles)
        for i in range(n//3, n , 2):
            total_coins += sorted_piles[i]

        return total_coins