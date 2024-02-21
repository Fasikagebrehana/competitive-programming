class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        steps = nums[0]
        for i in range(len(nums)):
            steps = max(steps, (i + nums[i]))
            if (steps + 1) >= len(nums):
                return True
            if steps == i:
                return False
        return False