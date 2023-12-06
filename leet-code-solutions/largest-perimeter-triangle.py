class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = sorted(nums, reverse = True)
        for i in range(len(n) - 2):
            if n[i] < n[i+1] + n[i+2]:
                return n[i] + n[i+1] + n[i+2]
        return 0
        