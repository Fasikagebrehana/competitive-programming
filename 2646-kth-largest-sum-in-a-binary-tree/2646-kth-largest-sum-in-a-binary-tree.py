# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        summ = []
        queue = deque([root])

        while queue:
            if root:
                s = 0
                for _ in range(len(queue)):
                    curr = queue.popleft()
                    s += curr.val
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                summ.append(s)
        
        summ.sort(reverse=True)
        if len(summ) < k:
            return -1
        return summ[k-1]