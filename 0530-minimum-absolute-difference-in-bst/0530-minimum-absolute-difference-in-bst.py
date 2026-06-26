# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = []
        def helper(root):
            if not root:
                return
            arr.append(root.val)
            helper(root.left)
            helper(root.right)
        
        helper(root)

        arr.sort()
        ans = inf
        for i in range(1, len(arr)):
            ans = min(ans, arr[i] - arr[i-1])
        return ans