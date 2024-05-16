# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def post(root):
            if not root:
                return
            if root.val == 0 or root.val == 1:
                return root.val == 1
            elif root.val == 2:
                return post(root.left) or post(root.right)
            elif root.val == 3:
                return post(root.left) and post(root.right)
            return False
        return post(root)