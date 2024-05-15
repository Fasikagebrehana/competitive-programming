class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        store = defaultdict(int)

        # ans = 0
        def dp(idx, summ): 
            if summ == amount:
                return 1
            if summ > amount:
                return 0
            if idx < 0:
                return 0
            if (idx, summ) not in store:
                store[(idx, summ)] = dp(idx, summ + coins[idx]) + dp(idx - 1, summ)
            return store[(idx, summ)]
        return dp(len(coins) - 1, 0)