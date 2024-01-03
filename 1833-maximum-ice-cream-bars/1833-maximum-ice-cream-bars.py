class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        icecream = 0
        s = 0
        costs.sort()
        for c in costs:
            s += c
            if s <= coins:
                icecream += 1
        return icecream