class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        removed = 0
        stack = []
        for i in range(len(nums)):
            if not stack:
                stack.append(nums[i])
            else:
                if stack[-1] == nums[i] and (len(stack) - 1) % 2 == 0:
                    removed += 1
                else:
                    stack.append(nums[i])
        if len(stack) % 2 != 0:
            removed += 1
        # print(stack, removed)

        return removed