"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # traverse by level what will change is its going tobe the childrens
        def helper(root):
            if not root:
                return 0
            maxDepth = 0
            
            for child in root.children:
                currDepth = helper(child)
                # print(child.val)
                maxDepth = max(maxDepth, currDepth)
            return 1 + maxDepth
        
        return helper(root)