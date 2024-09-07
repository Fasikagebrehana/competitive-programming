# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        half = head
        length = 0
        while half:
            length += 1
            half = half.next
        middle = length // 2
        ptr = head
        l = 0
        while ptr and l < middle:
            ptr = ptr.next
            l += 1
        prev = None
        right = ptr
        while right:
            right.next, prev, right = prev, right, right.next
        head2 = prev
        
        ans = head
        left = head
        leng = 0
        while leng < middle:
            if left:
                # print(left.val, 2)
                temp = left.next
                ans.next = left
                left = temp
                ans = ans.next
            if head2:
                t = head2.next
                ans.next = head2
                head2 = t
                ans = ans.next
            leng += 1
