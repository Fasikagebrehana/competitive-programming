# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        prev = head
        curr = head.next
        arr = []
        idx = 1
        while curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val):
                arr.append(idx)
            prev = curr
            curr = curr.next
            
            idx += 1
        if len(arr) < 2:
            return [-1, -1]
        min_dis, max_dis = inf, arr[-1] - arr[0]
        for i in range(len(arr)-1):
            min_dis = min(min_dis, abs(arr[i] - arr[i+1]))
           
        return [min_dis, max_dis]
