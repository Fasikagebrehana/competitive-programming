class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        arr = []
        nums.sort()
        def helper(idx):
            if arr[:] not in ans:
                ans.append(arr[:])
            for i in range(idx, len(nums)):
                # if arr in arr:
                #     continue
                arr.append(nums[i])
                helper(i+1)
                arr.pop()
        helper(0)
        return ans