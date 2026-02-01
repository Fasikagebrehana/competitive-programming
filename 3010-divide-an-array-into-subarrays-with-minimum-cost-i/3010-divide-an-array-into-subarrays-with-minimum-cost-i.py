class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        answer = nums[0]
        # we just need to add the 2 smallest numbers in nums[1:]

        num = sorted(nums[1:])
        return answer + num[0] + num[1]