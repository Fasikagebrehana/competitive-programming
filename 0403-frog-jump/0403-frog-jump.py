class Solution:
    def canCross(self, stones: List[int]) -> bool:
        store = defaultdict(int)
        if stones[1] != 1:
            return False
        def dp(i, k):
            if i == stones[len(stones) - 1]:
                return True
            
            if i not in stones:
                return False

            if (i, k) not in store:
                temp1 = tenp2 = temp3 = False
                if (i + k - 1) > i:
                    temp1 = dp(i + k - 1, k - 1)
                if (i + k) > i:
                    temp2 = dp(i + k, k)
                if (i + k + 1) > i:
                    temp3 = dp(i + k + 1, k + 1)
                store[(i, k)] = temp1 or temp2 or temp3
            return store[(i, k)]

        return dp(1, 1)