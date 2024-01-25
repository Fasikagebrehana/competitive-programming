# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        slow = head 
        fast = head.next
        ptr = fast
        while fast and fast.next:
            slow.next = fast.next
            slow = fast.next
            fast.next = slow.next
            fast = slow.next
        slow.next = ptr
        return head