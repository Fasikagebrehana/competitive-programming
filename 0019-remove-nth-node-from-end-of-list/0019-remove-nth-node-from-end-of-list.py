# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        prev = None
        l = 0
        while curr:
            l += 1
            curr = curr.next
        # print(l)
        count = 1
        curr = head
        if l == 1 and n == 1:
            return None

        while curr:
            if count == (l - n + 1):
                if curr.next:
                    temp = curr.next
                else:
                    temp = None
                if prev == None:
                    prev = temp
                    head = prev
                else:
                    prev.next = temp
                curr = temp
            else:
                temp =  curr.next
                prev = curr
                curr = temp
            count += 1
                


        # print(head)
        return head