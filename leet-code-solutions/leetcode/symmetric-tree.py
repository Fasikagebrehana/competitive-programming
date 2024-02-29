# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def helper(root1, root2):
            if not root1 and not root2:
                return True
            elif not root1 or not root2:
                return False
            else:
                if root1.val != root2.val:
                    return False
                return helper(root1.left, root2.right) and helper(root1.right, root2.left)
            
        return helper(root.left, root.right)