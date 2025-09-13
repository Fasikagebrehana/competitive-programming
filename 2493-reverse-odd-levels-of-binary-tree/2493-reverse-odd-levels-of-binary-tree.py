# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # we reverse the value not the node itself
        queue = deque([(root, 0)])
        level_arr = []
        while queue:

            for _ in range(len(queue)):
                node, level = queue.popleft()
                level_arr.append(node)

                if node.left:
                    queue.append((node.left, level+1))
                if node.right:
                    queue.append((node.right, level+ 1))
        
            if level % 2 != 0:
                l, r = 0, len(level_arr) - 1
                while l < r:
                    level_arr[l].val, level_arr[r].val = level_arr[r].val, level_arr[l].val
                    l+= 1
                    r -= 1
            level_arr = []
        return root