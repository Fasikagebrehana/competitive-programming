class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        subset = [[]]
        arr = []
        nums.sort()
        def backtrack(idx):
            nonlocal subset, arr
            if idx >= len(nums):
                return

            for i in range(idx, len(nums)):
                arr.append(nums[i])
                backtrack(i+1)
                if arr not in subset:
                    subset.append(arr[:])
                arr.pop()

        backtrack(0)
        # print(subset)
        return subset