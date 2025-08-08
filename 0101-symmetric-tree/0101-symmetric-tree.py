# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # iteratively using Queue
        if not root:
            return True
        queue = deque()
        queue.append((root.left, root.right))

        while queue:
            leftnode, rightnode = queue.popleft()

            if not leftnode and not rightnode:
                continue
            if not leftnode or not rightnode:
                return False
            
            if leftnode.val != rightnode.val:
                return False
            
            queue.append((leftnode.left, rightnode.right))
            queue.append((leftnode.right, rightnode.left))
        return True