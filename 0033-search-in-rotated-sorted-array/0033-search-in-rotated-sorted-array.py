class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            elif nums[left] <= nums[middle]:
                if nums[left] <= target and target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle  + 1

            elif nums[right] >= nums[middle]:
                if target <= nums[right] and nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
            

        return -1
