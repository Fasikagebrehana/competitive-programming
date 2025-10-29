# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # we need n-k and kth nodes
        # we need to make the n-kth next = None
        # the last element next to be the first

        if k == 0 or not head:
            return head

        curr = head
        n = 0
        last = None
        while curr:
            n += 1
            last = curr
            curr = curr.next
        # print(curr, n)
        m =  k % n
        if n == 1 or m == 0:
            return head
        

        curr = head
        prev = None
        idx = 0
        while curr:
            prev = curr
            curr = curr.next
            idx += 1
            if (n-m) == idx:
                prev.next = None
                last.next = head
                break
        return curr