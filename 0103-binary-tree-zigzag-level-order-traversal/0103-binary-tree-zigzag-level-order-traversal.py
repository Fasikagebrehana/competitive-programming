# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(root, True)])
        level_arr = []
        answer = []
        while queue:
            for _ in range(len(queue)):
                node, flag = queue.popleft()
                level_arr.append(node.val)
                if node.left:
                    queue.append((node.left, not flag))
                
                if node.right:
                    queue.append((node.right, not flag))
            if not flag:
                answer.append(level_arr[::-1])
            else:
                answer.append(level_arr[:])
            level_arr = []
        return answer