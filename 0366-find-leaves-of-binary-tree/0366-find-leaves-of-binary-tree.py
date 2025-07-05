# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        leaves = []
        answer = []
        def dfs(root):
            nonlocal leaves
            if not root:
                return
            if not root.left and not root.right:
                leaves.append(root.val)
                return None
                
            
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            
            return root

        while root:
            root = dfs(root)
            answer.append(leaves.copy())
            leaves = []
        # print(answer)
        return answer