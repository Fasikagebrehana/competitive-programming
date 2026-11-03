class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxx = max(nums)
        min_total = 0
        for num in nums:
            min_total += maxx - num

        return min_total