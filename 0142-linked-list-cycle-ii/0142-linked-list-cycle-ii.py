# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        cycle = set()
        while curr:
            if curr in cycle:
                return curr
            cycle.add(curr)
            curr = curr.next
        return None