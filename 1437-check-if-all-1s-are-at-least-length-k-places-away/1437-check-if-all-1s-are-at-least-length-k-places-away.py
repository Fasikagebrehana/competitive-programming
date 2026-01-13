class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        diff = 0
        if len(nums) == 1:
            return True
        if 1 not in nums:
            return True
        firstIndex = nums.index(1)
        numsRev = nums[::-1]
        lastIndex = len(nums) - numsRev.index(1) - 1
        # print(firstIndex)
        for i in range(len(nums)):
            if i == firstIndex:
                diff = 0
            elif nums[i] == 1 and diff < k:
                return False
            elif nums[i] == 0:
                diff += 1
            elif nums[i] == 1 and diff >= k:
                diff = 0
        return True