# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        min_depth = inf

        def helper(root, depth):
            nonlocal min_depth
            if not root:
                return
            if not root.left and not root.right:
                min_depth = min(min_depth, depth)
            
            if root.left:
                helper(root.left, depth + 1)
            if root.right:
                helper(root.right, depth + 1)
        
        helper(root, 1)
        # print(min_depth)
        return min_depth if min_depth != inf else 0