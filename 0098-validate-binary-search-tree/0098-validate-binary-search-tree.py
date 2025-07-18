# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        if not root:
            return

        def helper(root):
            nonlocal arr

            if not root:
                return True

            if root.left:
                left = helper(root.left)

            arr.append(root.val)

            if root.right:
                right = helper(root.right)

            
        helper(root)
        if len(arr) == len(set(arr)) and sorted(arr) == arr:
            return True
        return False