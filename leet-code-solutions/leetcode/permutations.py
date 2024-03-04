class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(arr):
            if len(arr) == len(nums):
                ans.append(arr[:])
                return
            for i in range(len(nums)):
                if nums[i] in arr:
                    continue
                arr.append(nums[i])
                helper(arr)
                arr.pop()
        helper([])
        return ans