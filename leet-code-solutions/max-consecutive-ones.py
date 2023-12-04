class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_one = 0
        n = len(nums)
        if n == 1 and nums[0] == 1:
            return 1
        elif n == 1 and nums[0] == 0:
            return max_one
        else:
            l, r = 0,  0
            curr = 0
            while r < len(nums):
                if nums[r] == 1:
                    curr += 1
                    r += 1
                    
                else:
                    curr = 0
                    r += 1
                max_one = max(max_one, curr)    
                
                
        return max_one
        