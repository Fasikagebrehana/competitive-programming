class Solution:
    def maxProduct(self, n: int) -> int:
        nums = []
        for digit in str(n):
            nums.append(int(digit))
        
        nums.sort(reverse = True)
        return nums[0] * nums[1]