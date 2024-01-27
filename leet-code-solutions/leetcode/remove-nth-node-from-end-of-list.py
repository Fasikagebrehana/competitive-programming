# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        deleted = head
        prev = None
        if not curr or not deleted or not head.next:
            return
        idx = 0
        while curr and idx < n - 1:
            curr = curr.next
            idx += 1
        if not curr:
            return head.next
        while curr and curr.next:
            curr = curr.next
            prev = deleted
            deleted = deleted.next
        if prev and deleted:
            prev.next = deleted.next
        else:
            head = head.next
        return head
        