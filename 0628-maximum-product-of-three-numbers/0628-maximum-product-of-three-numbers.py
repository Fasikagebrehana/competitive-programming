class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        maxx = -inf
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            maxx = max(maxx, nums[i] * nums[i+1] *nums[n-1])
            # print(nums[i], nums[i+1], nums[n-1])

        return maxx