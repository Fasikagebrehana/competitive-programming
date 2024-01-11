class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, 0
        while l < len(nums):
            if nums[l] != val:
                nums[r] = nums[l]
                r += 1
            l += 1
        return r