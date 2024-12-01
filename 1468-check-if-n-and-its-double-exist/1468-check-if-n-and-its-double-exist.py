class Solution:
    def checkIfExist(self, nums: List[int]) -> bool:
        if 0 in nums and nums.count(0) > 1:
            return True
        for num in nums:
            if num/2 in nums and num != 0:
                return True
        return False