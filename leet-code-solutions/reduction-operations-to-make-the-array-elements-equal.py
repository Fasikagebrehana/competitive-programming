class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        s = 0
        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                s += i
        return s