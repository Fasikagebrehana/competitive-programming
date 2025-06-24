class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        operation = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            t = nums[i]
            for j in range(i, len(nums)):
                temp = nums[j] - t
                if temp < 0:
                    nums[j] = 0
                else:
                    nums[j] =  temp
            operation += 1
            # print(nums)
        return operation
