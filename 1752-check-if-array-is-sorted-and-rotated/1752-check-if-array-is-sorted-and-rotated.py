class Solution:
    def check(self, nums: List[int]) -> bool:
        # 5 2 1 3 4
        changes = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                changes += 1
                if changes > 1:
                    return False
        if nums[0] < nums[-1]:
            changes += 1
        return False if changes > 1 else True