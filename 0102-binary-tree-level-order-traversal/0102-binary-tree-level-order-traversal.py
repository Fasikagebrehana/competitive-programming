# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        Level_arr = []
        answer = []
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                Level_arr.append(node.val)
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
        # print(answer)
            answer.append(Level_arr[:])
            Level_arr = []
        return answer