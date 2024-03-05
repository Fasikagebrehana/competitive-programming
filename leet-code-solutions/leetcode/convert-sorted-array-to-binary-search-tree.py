# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def BST(left, right):
            if left > right:
                return 
            middle = (left + right) // 2
            start = BST(left, middle - 1)
            end = BST(middle + 1, right)
            return TreeNode(nums[middle], start, end)
        return BST(0, len(nums)-1)