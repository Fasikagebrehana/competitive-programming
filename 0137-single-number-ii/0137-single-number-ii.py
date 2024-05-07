class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        v1, v2 = 0, 0
        for num in nums:
            v1 = (num ^ v1) & ~(v2)
            v2 = (num ^ v2) & ~(v1)
        return v1