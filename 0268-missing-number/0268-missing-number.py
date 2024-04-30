class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = [i for i in range(len(nums) + 1)]
        nums.extend(arr)
        res = nums[0] ^ nums[1]
        for i in range(2, len(nums)):
            res = res ^ nums[i]
        return res     