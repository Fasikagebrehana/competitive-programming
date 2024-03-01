# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        dic = defaultdict(list)
        def helper(root, depth):
            if not root:
                return
            dic[depth].append(root.val)
            
            
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)
            # depth = 0
        helper(root, 0)
        print(dic)
        for key, val in dic.items():
            if key % 2:
                ans.append(val[::-1])
            else:
                ans.append(val)
        return ans