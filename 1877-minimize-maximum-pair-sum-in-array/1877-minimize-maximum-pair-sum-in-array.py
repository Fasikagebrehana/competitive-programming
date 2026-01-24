class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        minMaxSum = 0
        nums.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            minMaxSum = max(minMaxSum, nums[i] + nums[j])
            i += 1
            j -= 1
        
        return minMaxSum