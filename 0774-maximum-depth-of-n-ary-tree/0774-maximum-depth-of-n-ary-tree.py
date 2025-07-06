"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        level = 0
        queue = deque([(root, level)])
        max_depth = 0
        while queue:
            
            for _ in range(len(queue)):
                node, level = queue.popleft()
                max_depth = max(max_depth, level)
                for child in node.children:
                    queue.append((child, level + 1))
        # print(max_depth + 1)

        return max_depth + 1