# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        # print(n)
        if n == 1:
            return None
        mid = n // 2
        prev = None
        curr = head
        n = 0
        while curr:
            if n == mid:
                temp = curr
                prev.next = temp.next
                curr = temp.next
                break
            else:
                temp = curr
                prev = temp
                curr = curr.next
            n +=1
        # print(head)
        return head