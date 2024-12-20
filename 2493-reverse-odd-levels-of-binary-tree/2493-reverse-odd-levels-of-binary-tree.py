# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([(root, 0)])

        while queue:
            i, j = 0, len(queue) - 1
            # print(queue[0][0])
            node, level = queue[0]
            if level % 2 != 0:
                while i < j:
                    val1, l1 = queue[i]
                    val2, l2 = queue[j]
                    val1.val, val2.val = val2.val, val1.val
                    i += 1
                    j -= 1
            for _ in range(len(queue)):
                node, level = queue.popleft()
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))
        return root
            