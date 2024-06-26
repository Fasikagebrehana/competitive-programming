# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(root, summ):
            if not root:
                return False
            summ += root.val
            if root.left == None and root.right == None:
                if summ == targetSum:
                    return True
                else:
                    return False
            return helper(root.left, summ) or helper(root.right, summ)
            
            
            
        return helper(root, 0)
