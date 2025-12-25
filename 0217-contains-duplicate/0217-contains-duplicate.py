class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinct = len(set(nums))
        return True if distinct != len(nums) else False