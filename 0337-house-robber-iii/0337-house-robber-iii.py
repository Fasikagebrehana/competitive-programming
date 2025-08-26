# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dp(root):
            if not root:
                return 0

            if root in memo:
                return memo[root]
            
            money_with_curr = root.val
            if root.left:
                money_with_curr += dp(root.left.left) + dp(root.left.right)
            if root.right:
                money_with_curr += dp(root.right.right) + dp(root.right.left)
            money_without_curr = dp(root.left) + dp(root.right)
            
            memo[root] = max(money_with_curr, money_without_curr)

            return memo[root]
        return dp(root)