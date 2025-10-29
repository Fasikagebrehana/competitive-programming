# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # we need 4 things before reverse: start, startprev, endnext and end
        # we need to modularize which means creating our reverse function 
        dummy = ListNode(0)

        def reverse(curr):
            # curr = head
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
            # print(prev)
        dummy.next = head
        curr = head
        prev = dummy
        start = head
        n = 0
        while curr:
            n += 1
            if n == k:
                # print(n)
                end = curr
                curr = curr.next
                endnext = curr
                # print(curr)
                end.next = None

                node = reverse(start)
                start.next = endnext
                # print(start)

                prev.next = node

                prev = start
                start = curr
                n = 0
            else:
                curr = curr.next
        # print(head)
        # print(curr)
        # print(dummy)
        return dummy.next