class Solution:
    def integerBreak(self, n: int) -> int:
        store = defaultdict(int)
        if n < 4:
            return n - 1
        def dp(num):
            if num < 4:
                return num
            
            if num not in store:
                for i in range(1, n + 1):
                    store[num] = max(store[num], i * dp(num - i))

            return store[num]
        return dp(n)