class Solution:
    def findMin(self, nums: List[int]) -> int:


        left, right = 0, len(nums) -1
        if left == right:
            return nums[0]
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > nums[right]:
                left = middle+1
            elif nums[right] > nums[middle]:
                right = middle
            else:
                right -= 1
        return nums[right]