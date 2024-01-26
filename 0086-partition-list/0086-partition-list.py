# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        while curr and curr.val < x:
            prev = curr
            curr = curr.next
            
        if curr is None or curr.next is None:
            return head
        
        while curr and curr.next:
            if curr.next.val < x:
                temp = curr.next
                curr.next = curr.next.next
                temp.next = prev.next
                prev.next = temp
                prev = prev.next
            else:
                curr = curr.next
        return dummy.next