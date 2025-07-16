class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = 1
        suffix = 1
        maxx = 0
        if len(nums) == 1:
            return nums[-1]
        for i in range(len(nums)):
            #  prefix becomes 0 means nums[i] == 0 we don't need the multiplication with 0 because it will become 0
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            
            prefix = prefix * nums[i]
            suffix = suffix * nums[len(nums) - 1 - i]
    
            maxx = max(maxx, max(prefix, suffix))
        return maxx