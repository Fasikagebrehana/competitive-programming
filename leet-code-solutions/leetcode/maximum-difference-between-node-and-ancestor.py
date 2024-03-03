# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        minNode, maxNode = inf, 0
        def helper(root, minNode, maxNode):
            nonlocal ans
            if not root:
                ans = max(ans, abs(maxNode - minNode))
                return ans
            helper(root.left, min(minNode, root.val), max(maxNode, root.val))
            helper(root.right, min(minNode, root.val), max(maxNode, root.val))
        helper(root, minNode, maxNode)
        return ans