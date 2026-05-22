class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) -1

        while left <= right:
            middle = (left + right) // 2
            
            if nums[middle] == target:
                return True
            
            if nums[middle] == nums[left]:
                left += 1
                continue
            
            elif nums[left] <= nums[middle]:
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1

            elif nums[right] >= nums[middle]:
                if nums[right] >= target > nums[middle]:
                    left = middle + 1
                else:
                    right = middle - 1
        
        return False