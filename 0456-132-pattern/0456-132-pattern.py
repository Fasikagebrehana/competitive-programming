class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # using monotonic decreasing stack
        # its like finding the biggest number and the middle number using strictly decreasing number then lastly finding the smallest number
        stack = []
        thirdNum = -inf
        for i in range(len(nums) - 1, -1, -1):
            while stack and stack[-1] < nums[i]:
                thirdNum =  stack.pop()
            if stack and stack[-1] > nums[i]:
                if thirdNum != -inf and nums[i] < thirdNum:
                    return True
            stack.append(nums[i])
        return False