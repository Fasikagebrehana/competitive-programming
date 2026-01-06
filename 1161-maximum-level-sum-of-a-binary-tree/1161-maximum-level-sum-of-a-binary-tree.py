# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 1)])
        max_sum = -inf
        max_sum_level = 0
        summ = 0
        while queue:
            if not root:
                return
            
            
            for _ in range(len(queue)):
                node, level = queue.popleft()
                summ += node.val
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))

            if summ > max_sum:
                max_sum = summ
                max_sum_level = level
            # print(summ)
            summ = 0
        # print(max_sum, max_sum_level)
        return max_sum_level