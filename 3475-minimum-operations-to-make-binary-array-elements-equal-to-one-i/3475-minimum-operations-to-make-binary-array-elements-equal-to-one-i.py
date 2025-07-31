class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if (i + 2) < len(nums):
                    nums[i] = 1
                    nums[i+1] = 1 if nums[i+1] == 0 else 0
                    nums[i+2] = 1 if nums[i+2] == 0 else 0
                    operations += 1
        # print(nums)

        return operations if len(nums) == sum(nums) else -1