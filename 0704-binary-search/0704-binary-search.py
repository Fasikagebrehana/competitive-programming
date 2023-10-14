class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        top = n-1
        bottom = 0
        while top >= bottom:
            middle = int((top + bottom) / 2)
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                top = middle - 1
            else:
                bottom = middle + 1
        return -1
            
        