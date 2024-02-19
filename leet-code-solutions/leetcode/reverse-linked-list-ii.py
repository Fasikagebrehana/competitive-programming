# Definition for singly-linked list.
# class ListNode:
#     def __init__(sel                                                                                                      vvvvvvv              v              f, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = head
        prev = dummy
        prevprev  = start = None
        i = 1
        while i <= right:
            if i <= left:
                prevprev = prev
                start = curr
                prev = prev.next
                curr = curr.next
                
                
            else:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            i += 1
            
        prevprev.next = prev
        start.next = curr
        return dummy.next
        