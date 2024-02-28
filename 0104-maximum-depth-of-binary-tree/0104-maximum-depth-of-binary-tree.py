# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
#         depth = [0]
#         max_depth = [0]
#         temp = root
#         def helper(root, depth, max_depth):
#             if root.left:
#                 helper(root.left, depth, max_depth)
#                 depth[0] += 1
#                 if temp == root.left.val:
#                     max_depth[0] = max(max_depth[0], depth[0])
#                     depth = [0]
#             if root.right:
#                 helper(root.right, depth, max_depth)
#                 depth[0] += 1
#                 if temp == root.right.val:
#                     max_depth[0] = max(max_depth[0], depth[0])
#                     depth = [0]
        # helper(root, depth, max_depth)
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

            