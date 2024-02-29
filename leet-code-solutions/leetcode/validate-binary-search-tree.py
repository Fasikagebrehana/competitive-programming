# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root, mini, maxi):
            if not root:
                return True
            if root.val >= maxi or root.val <= mini:
                return False
            return helper(root.left, mini, root.val) and helper(root.right, root.val, maxi)
            
            
        return helper(root, -inf, inf)
        
        
        
#         def helper(root):
#             if root.right:
#                 while root.right:
#                     root = root.right
#             return root.val
        
#         def helper1(root):
#             if root.left:
#                 while root.left:
#                     root = root.left
#             return root.val
#         if root.left:
#             leftMax = helper(root.left)
#         else:
#             leftMax = root.val
#         if root.right:
#             rightMin = helper1(root.right)
#         else:
#             rightMin = root.val
        
#         if leftMax > root.val or rightMin < root.val:
#             return False
        
#         left = self.isValidBST(root.left)        
#         right = self.isValidBST(root.right)
        
#         if left == True and right == True:
#             return True
#         else:
#             return False
