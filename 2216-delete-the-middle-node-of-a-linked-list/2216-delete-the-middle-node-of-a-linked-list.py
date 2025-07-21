# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        prev = None
        while fast and fast.next:
            temp = slow.next
            prev = slow
            slow = temp
            if fast.next.next:
                fast = fast.next.next
            else:
                fast = None
        
        # print(prev)
        if not prev:
            return None
        temp = slow.next
        prev.next = temp
        # print(head)
        return head