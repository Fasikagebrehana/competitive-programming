# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def divide(nums):
            if len(nums) == 1:
                return TreeNode(nums[0])
            if len(nums) == 0:
                return
            maxNums = nums.index(max(nums))
            left = divide(nums[:maxNums])
            right = divide(nums[maxNums + 1:])
            return TreeNode(nums[maxNums], left, right)
        
        return divide(nums)