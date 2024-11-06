class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        for j in range(len(nums)):
            for i in range(1, len(nums)):
                a = bin(nums[i-1])[2:]
                b = bin(nums[i])[2:]
                if nums[i] < nums[i-1]:
                    if a.count('1') == b.count('1'):
                        nums[i-1], nums[i] = nums[i], nums[i-1]
        sorted_nums = sorted(nums)
        return sorted_nums == nums