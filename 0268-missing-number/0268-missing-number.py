class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0

        for num in nums:
            xor ^= num
        
        # missing = 0
        for i in range(0, n+1):
            xor ^= i
        return xor