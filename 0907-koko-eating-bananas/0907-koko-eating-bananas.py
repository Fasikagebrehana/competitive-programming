class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left, right = 1, piles[-1]
        summ = sum(piles)
        def helper(middle):
            time = 0
            for pile in piles:
                time += math.ceil(pile / middle)
                if time > h:
                    return False
            return True

        k = inf
        while left <= right:
            middle = (left + right) // 2
            if helper(middle):
                k = min(k, middle)
                right = middle - 1
            else:
                left = middle + 1
        # print(k)
        return k