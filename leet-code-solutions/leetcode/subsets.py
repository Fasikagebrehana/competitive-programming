class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        arr = []
        def helper(idx):
            ans.append(arr[:])
            for i in range(idx, len(nums)):
                arr.append(nums[i])
                helper(i+1)
                arr.pop()
        helper(0)
        return ans