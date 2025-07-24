# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        curr = head
        dummy = ListNode(0)
        ptr = dummy
        while curr:
            ans.append(curr.val)
            curr = curr.next
        ans.sort()
        for num in ans:
            newNode = ListNode(num)
            ptr.next = newNode
            ptr = ptr.next
        return dummy.next