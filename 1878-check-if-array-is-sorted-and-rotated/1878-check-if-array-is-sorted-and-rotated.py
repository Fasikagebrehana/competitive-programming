class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        if nums == sorted_nums:
            return True
        count = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                count += 1
            if count > 1:
                return False
        if nums[-1] > nums[0]:
            return False
        
        return True