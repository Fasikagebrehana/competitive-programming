# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head = prev
        curr = prev
        # prev = head
        carry = 0
        while curr:
            temp = curr.val * 2 + carry
            curr.val = temp % 10
            carry = temp // 10
            prev = curr
            curr = curr.next
        if carry > 0:
            prev.next = ListNode(carry)

        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev