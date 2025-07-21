# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return
        slow = head
        fast = head.next.next if head.next else None

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # print(slow)
        def reverse(curr):
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        # print(slow.next)
        curr = reverse(slow.next)
        # print(curr)

        prev = head
        while prev != slow.next and curr:
            if prev.val != curr.val:
                return False
            prev = prev.next
            curr = curr.next
        return True