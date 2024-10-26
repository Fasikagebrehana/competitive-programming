# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxWidth = 0
        queue = deque([(root, 0)])
        while queue:
            n, lastFirstIndex = queue[0]
            l = len(queue)
            
            for _ in range(l):
                node, level = queue.popleft()
                if node.left:
                    queue.append((node.left, level * 2))
                if node.right:
                    queue.append((node.right, 2 * level + 1))
            maxWidth = max(maxWidth, level - lastFirstIndex + 1)
        return maxWidth