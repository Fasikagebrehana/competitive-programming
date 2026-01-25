class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        minDiff = inf
        i, j = 0, k - 1
        if len(nums) == 1 or k == 1:
            return 0

        while j < len(nums):
            minDiff = min(minDiff, nums[j] - nums[i])
            i  += 1
            j += 1
            # print(minDiff)
        return minDiff