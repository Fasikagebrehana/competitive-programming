class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        temp = inf
        def helper(middle):
            time = 0
            banana = 0
            for i in range(len(piles)):
                time += math.ceil(piles[i] / middle) 
            if time > h:
                return False
            return True
        while high >= low:
            middle = (high + low) // 2
            if helper(middle):
                high = middle - 1
            else:
                low = middle + 1
        return low