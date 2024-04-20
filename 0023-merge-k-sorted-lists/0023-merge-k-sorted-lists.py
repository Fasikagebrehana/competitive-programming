# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        idx = 0
        for i in range(len(lists)):
            node = lists[i]
            if node:
                heappush(heap, (node.val, idx, node))
            idx += 1
        dummy = ListNode(0)
        ptr = dummy

        while heap:
            val, idx, node = heappop(heap)
            ptr.next = node
            ptr = ptr.next
            if node.next:
                heappush(heap, (node.next.val, idx, node.next))
        return dummy.next
