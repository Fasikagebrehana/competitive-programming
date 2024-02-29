# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root):
            if not root:
                return
            if root == p or root == q:
                return root
            left = helper(root.left)
            right = helper(root.right)
            if not right :
                return left
            elif not left:
                return right
            else:
                return root
        return helper(root)
            