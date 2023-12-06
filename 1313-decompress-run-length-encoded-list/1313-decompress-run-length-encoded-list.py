class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            if i*2 <len(nums):
                f = nums[i*2]
                v = nums[2 * i + 1]
                ans.extend([v]*f)
        return ans