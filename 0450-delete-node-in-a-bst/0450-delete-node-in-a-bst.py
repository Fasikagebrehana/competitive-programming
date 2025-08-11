# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # good strategy is to replace the tobe deleted val with the lowest value in the right branch of the tobedeleted node
        # but first we have to search the val

        if not root:
            return
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right =  self.deleteNode(root.right, key)
        else:
            # here we have 3 options, 1. if it has only left child
            # 2. it has only right child 3. both
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # if it has 2 branches we have to fing the minimum from the right child
                # successor = root
                successor = root.right
                while successor.left:
                    successor = successor.left
                root.val = successor.val
                root.right = self.deleteNode(root.right, root.val)
        return root