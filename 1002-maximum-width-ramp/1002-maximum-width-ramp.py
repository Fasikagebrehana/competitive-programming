class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_width = 0
        stack = [0]
        
        for i in range(len(nums)):
            if stack and nums[stack[-1]] > nums[i]:
                stack.append(i)
        # print(stack)

        for i in range(len(nums) - 1, -1, -1):
            # j = len(stack) - 1
            while stack and nums[i] >= nums[stack[-1]]:
                idx = stack.pop()
                max_width = max(max_width, (i - idx))
                # j -= 1
        return max_width