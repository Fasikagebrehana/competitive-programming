class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        modulo = 10 ** 9 + 7
        def helper(idx):
            temp = bisect_right(nums, target - nums[idx])
            if temp <= idx:
                if temp == idx and (nums[idx] + nums[idx]) <= target:
                    return 1
                else:
                    return 0
            return 2 ** (temp - idx - 1)
        
        count = 0
        for i in range(len(nums)):
            subsequence = helper(i)
            count += subsequence
        return count % modulo