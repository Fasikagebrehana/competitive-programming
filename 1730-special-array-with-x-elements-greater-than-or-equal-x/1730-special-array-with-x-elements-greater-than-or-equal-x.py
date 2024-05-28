class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(max(nums)+1):
            if (len(nums) - bisect_left(nums, i)) == i:
                return i
        return -1