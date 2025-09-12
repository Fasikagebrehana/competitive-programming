# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # odd indexed == even integers strictly decreasing
        # even indexed == odd integers strictly increasing
        # using bfs queue track the level

        queue = deque([(root, 1)])
        level_arr = []
        
        while queue:
            for _ in range(len(queue)):
                node, level = queue.popleft()
                if level % 2 == 0:
                    if node.val % 2 != 0:
                        return False
                    elif level_arr and level_arr[-1] <= node.val:
                        return False
                    else:
                        level_arr.append(node.val)
                else:
                    if node.val % 2 == 0:
                        return False
                    elif level_arr and level_arr[-1] >= node.val:
                        return False
                    else:
                        level_arr.append(node.val)
                
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))
            level_arr = []
        return True