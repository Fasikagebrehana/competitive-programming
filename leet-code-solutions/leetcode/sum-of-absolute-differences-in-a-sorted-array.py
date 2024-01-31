class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        n = len(nums)
        prefix[0] = nums[0]
        suffix[n-1] = nums[n-1]
        ans = []
        left_sum = 0
        right_sum = 0
        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] + nums[i]
            
        for i in range(n):
            left_sum = (i * nums[i]) - prefix[i-1] if i > 0 else 0
            right_sum = suffix[i+1] - (n-i-1) * nums[i] if i < n-1 else 0
            ans.append((left_sum + right_sum))
        return ans