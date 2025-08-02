class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        counter = defaultdict(int)
        for b1 in basket1:
            counter[b1] += 1
        for b2 in basket2:
            counter[b2] -= 1
            # if it already exists we are decrementing like balancing
            # if it gets to negative that means there is more b2 in basket2


        # compute by checking if counter val is odd it means there is noway
        # we can balance
        # else we can count what the share in each basket must be and save
        # the extra's found in each baskets
        extra = []
        for key, val in counter.items():
            if val % 2 != 0:
                return -1
            extra += [key] * abs(val // 2)
        # print(extra)

        # we only need to swap half length of extra elements
        # and we need to sort it 
        extra.sort()
        # other thing is we can swap an element with the mini element from
        # both baskets if minnvalue * 2 is less than the current value
        mincost = 0
        minValue = min(min(basket1), min(basket2))
        halfLen = len(extra) // 2
        for i in range(halfLen):
            mincost += min(extra[i], 2 * minValue)


        return mincost