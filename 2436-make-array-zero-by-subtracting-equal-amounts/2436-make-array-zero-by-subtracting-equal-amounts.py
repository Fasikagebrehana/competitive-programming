class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # print(len((nums)))
        num = list(set(nums))
        zeros = num.count(0)
        # print(zeros)
        if zeros == len(nums):
            return 0
        return len(set(nums)) - zeros