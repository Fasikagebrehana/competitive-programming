class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def helper(x, y):
            return x + y < y + x
        
        for i in range(len(nums)):
            for j in range(len(nums)-1-i):
                if helper(str(nums[j]), str(nums[j+1])):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        nums = int(''.join(str(num) for num in nums))
        return str(nums)