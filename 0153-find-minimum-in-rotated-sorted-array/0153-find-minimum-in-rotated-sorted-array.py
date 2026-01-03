class Solution:
    def findMin(self, nums: List[int]) -> int:
        # must find the pivot which is increase then decrease point
        # 45012
        # how do we know the number is minimum
        # middle is less than bothe left and right side of it return middle
        # middle > middle +1 left = middle +1 min middle + 1

        left, right = 0, len(nums) - 1
        minn = inf
        if left == right:
            return nums[left]

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] > nums[middle + 1]:
                return nums[middle + 1]

            elif nums[middle] < nums[middle - 1]:
                return nums[middle]

            # the above two cases are if its in the pivot points
            elif nums[middle] > nums[right]:
                left = middle + 1
            elif nums[middle] < nums[right]:
                right = middle - 1