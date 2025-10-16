# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # bst make it easier because since there is only p and q, and if p.val < root.val we go to the left and if q.val < root we traverse to left
        # if its greater we go to the right
        # if p is less than roo val and q is greater or vice verse it means the current is their lowest common ancestor

        def dfs(root):
            if not root:
                return
            if (p.val < root.val and q.val > root.val) or (p.val > root.val and q.val < root.val):
                return root
            elif p == root or q == root:
                return root
            elif (p.val < root.val and q.val < root.val):
                return dfs(root.left)
            else:
                return dfs(root.right)
        return dfs(root)