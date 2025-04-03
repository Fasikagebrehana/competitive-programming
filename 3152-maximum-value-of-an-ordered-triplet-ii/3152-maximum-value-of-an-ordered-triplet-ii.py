class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        max_difference = 0
        max_val = 0

        for n in nums:
            res = max(res, max_difference * n)
            max_difference = max(max_difference, max_val - n)
            max_val = max(max_val, n)
        return res