# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        summ = 0
        def helper(root, s):
            nonlocal summ
            if not root.left and not root.right:
                s += str(root.val)
                summ += int(s)
                return
            if root.left:
                helper(root.left, s + str(root.val))
            if root.right:
                helper(root.right, s + str(root.val))
        helper(root, "")
        return summ
            # nonlocal temp
            # nonlocal arr
            # nonlocal ans
            # if not root:
            #     return
            # arr.append(root.val)

            # left = helper(root.left)
            # print(ans, arr, "fg")
            # temp = ''.join(str(n) for n in arr)
            # ans.append(int(temp))

            # right = helper(root.right)
            # temp = ''.join(str(n) for n in arr)
            # ans.append(int(temp))
            # arr = []

        # helper(root)
        # print(ans)
        # return 0
