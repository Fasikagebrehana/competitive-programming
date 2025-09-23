class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        arr = []
        result = []

        def backtrack(idx):
            if len(arr) == len(nums):
                result.append(arr[:])
                return
            
            if len(arr) > len(nums):
                return
            
            for i in range(len(nums)):
                if nums[i] not in arr:
                    arr.append(nums[i])
                    backtrack(i+1)
                    arr.pop()

        backtrack(0)
        # print(result)
        return result