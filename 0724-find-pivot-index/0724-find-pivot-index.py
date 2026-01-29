class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSumm = sum(nums)
        movingSum = 0

        for i in range(len(nums)):
            totalSumm -= nums[i]
            if totalSumm == movingSum:
                return i
            movingSum += nums[i]

        return -1