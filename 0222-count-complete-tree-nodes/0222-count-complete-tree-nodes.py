# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        arr = []
        def preorder(root):
            nonlocal arr
            if not root:
                return
            arr.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return len(arr)