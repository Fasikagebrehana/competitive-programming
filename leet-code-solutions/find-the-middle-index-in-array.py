class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftmost = 0
        for i in range(len(nums)):
            n = nums[i]
            rightmost = total - leftmost - n
            if leftmost == rightmost:
                return i
            leftmost += n
        return -1