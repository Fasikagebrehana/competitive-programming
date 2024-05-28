class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        store = defaultdict(int)
        
        def dp(i, j):
            minn = inf
            if (i, j) not in store:
                for k in range(i + 1, j):
                    minn = min(values[i] * values[j] * values[k] + dp(i, k) + dp(k, j),minn)
                store[(i, j)] = minn if minn != inf else 0
            return store[(i, j)]
        return dp(0, len(values) - 1)