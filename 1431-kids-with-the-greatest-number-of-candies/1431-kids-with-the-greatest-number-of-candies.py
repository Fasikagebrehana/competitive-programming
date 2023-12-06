class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        max_candy = max(candies)
        for i in range(len(candies)):
            curr_sum = candies[i] + extraCandies
            if curr_sum >= max_candy:
                ans.append(True)
            else:
                ans.append(False)
        return ans