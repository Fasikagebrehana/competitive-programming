# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic = defaultdict(int)
        def helper(root):
            if not root:
                return
            dic[root.val] += 1
            helper(root.left)
            helper(root.right)
        helper(root)
        if dic:
            mode = max(dic.values())
        return [node for node, count in dic.items() if mode == count]