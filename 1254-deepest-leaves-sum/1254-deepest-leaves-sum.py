# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # last level nodes value sum
        # go level order traversal
        if not root:
            return 0
        queue = deque([root,])
        arr = []
        levels = []
        while queue:

            for _ in range(len(queue)):
                node = queue.popleft()
                
                levels.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            arr.append(levels)
            levels = []

        deepest_summ = 0
        # print(arr[-1])
        for num in arr[-1]:
            deepest_summ += num
        return deepest_summ