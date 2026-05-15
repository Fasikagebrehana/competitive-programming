class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 4,5,6,7,8,1,2
        # 7//2=3
        # [3]=7

        left, right = 0, len(nums) -1
        if left == right:
            return nums[0]
        while left <= right:
            middle = (left + right) // 2
            if nums[middle -1] > nums[middle]:
                return nums[middle]
            if nums[middle+1] < nums[middle]:
                return nums[middle+1]
            if nums[middle] > nums[right]:
                left = middle+1
            elif nums[right] > nums[middle]:
                right = middle-1
        