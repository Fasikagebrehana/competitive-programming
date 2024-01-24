# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        currnode = head
        
        while currnode:
            temp = currnode.next
            currnode.next = prev
            prev = currnode
            currnode = temp
        return prev