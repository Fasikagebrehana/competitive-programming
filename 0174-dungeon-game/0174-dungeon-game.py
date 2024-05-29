class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        store = defaultdict(int)
        n, m = len(dungeon[0]), len(dungeon)
        def dp(i, j):
            if i == m-1 and j == n-1:
                return dungeon[m-1][n-1] if dungeon[m-1][n-1] < 0 else 0
            if i >= m or j >= n:
                return -inf
            
            if (i, j) not in store:
                temp = dungeon[i][j] + max(dp(i, j+1), dp(i+1, j))
                if temp > 0:
                    store[(i, j)] = 0
                else:
                    store[(i, j)] = temp
            return store[(i, j)]
        return (abs(dp(0,0)) + 1)