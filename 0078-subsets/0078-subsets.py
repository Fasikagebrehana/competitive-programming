class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # using backtracking algorithm
        subset = [[]]
        arr = [] #to store the current subset
        def backtrack(idx):
            nonlocal subset, arr

            if idx > len(nums):
                return
            
            for i in range(idx, len(nums)):
                
                arr.append(nums[i])
                backtrack(i+1)
                subset.append(arr[:])
                arr.pop()
                
        backtrack(0)
        return subset