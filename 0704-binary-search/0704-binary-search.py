class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        index = -1
        top = n-1
        bottom = 0
        while top >= bottom:
            middle = int((top + bottom) / 2)
            if target == nums[middle]:
                index = middle
                break
            else:
                if target < nums[middle]:
                    top = middle - 1
                else:
                    bottom = middle + 1
            if index == -1 and top >= bottom:
                index=-1
        return index
            
        