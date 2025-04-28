class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        if high == low:
            return nums[low]
        while high >= low:
            middle = (low + high) // 2
            if nums[middle + 1] < nums[middle]:
                return nums[middle + 1]
            elif nums[middle] < nums[middle - 1]:
                return nums[middle]
            elif nums[high] > nums[middle]:
                high = middle - 1
            elif nums[high] < nums[middle]:
                low = middle + 1
