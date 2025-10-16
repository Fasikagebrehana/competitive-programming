# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(root):
            if not root:
                return
            
            if root == p:
                return p
            elif root == q:
                return q

            left = dfs(root.left)
            right = dfs(root.right)
            if left and right:
                return root
            elif left:
                return left
            return right
        
            
        # print(dfs(root))
        return dfs(root)