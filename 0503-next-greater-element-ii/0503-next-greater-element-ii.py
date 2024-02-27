class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(nums)
        stack.append((0, nums[0]))
        for i in range(1, len(nums)):
            while stack and nums[i] > stack[-1][1]:
                temp = stack.pop()
                ans[temp[0]] = nums[i]
            stack.append((i, nums[i]))
        
        for idx, val in stack:
            i = 0
            while i < len(nums) and val >= nums[i]:
                i += 1
            if i < len(nums):
                ans[idx]  = nums[i]
            
        return ans