# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        summ = 0
        def helper(root):
            nonlocal summ
            if not root:
                return
            if root.val <= high and root.val >= low:
                summ += root.val
            helper(root.left)
            helper(root.right)
        helper(root)
        return summ