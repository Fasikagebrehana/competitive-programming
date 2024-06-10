class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        l, r = 0, 1
        while r < len(nums) and l < len(nums):
            ans.append(nums[r])
            ans.append(nums[l])
            l += 2
            r += 2
        return ans