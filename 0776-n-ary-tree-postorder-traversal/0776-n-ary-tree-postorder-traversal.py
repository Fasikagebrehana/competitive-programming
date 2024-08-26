"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        arr = []
        def helper(root):
            nonlocal arr
            if not root:
                return
            
            for node in root.children:
                helper(node)

            arr.append(root.val)
        helper(root)
        return arr
        