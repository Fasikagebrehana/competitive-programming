# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dic = defaultdict(int)
        curr = headA
        # i = 0
        while curr:
            dic[curr] += 1
            curr = curr.next
            # i += 1
        currnode = headB
        while currnode:
            if dic[currnode] > 0:
                return currnode
            currnode = currnode.next
        