class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = Counter(nums)
        for key in Counter(nums):
            if n[key] > 1:
                return True
        return False