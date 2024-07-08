# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head.next
        summ = 0
        dummy = ListNode(0)
        ptr = dummy
        while curr:
            if curr.val != 0:
                summ += curr.val
            else:
                ptr.next = ListNode(summ)
                ptr = ptr.next
                summ = 0
            curr = curr.next
        return dummy.next
