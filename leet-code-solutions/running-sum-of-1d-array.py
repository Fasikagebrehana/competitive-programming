class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        i=1
        while i < len(nums):
            nums[i]=nums[i-1]+nums[i]
            i += 1
        
        return nums;