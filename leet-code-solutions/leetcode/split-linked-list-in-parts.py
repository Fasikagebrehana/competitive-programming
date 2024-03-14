# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        n = length // k
        r = length % k
        currnode = head
        ans = []
        ptr = 1
        prev = head
        print(n, r)
        while currnode:
            if r > 0 and ptr == (n + 1):
                ans.append(prev)
                ptr = 1
                r -= 1
                prev = currnode.next
                currnode.next = None
                currnode = prev
            elif r == 0 and ptr == n:
                ans.append(prev)
                ptr = 1
                prev = currnode.next
                currnode.next = None
                currnode = prev
            else:
                currnode = currnode.next
                ptr += 1
        x = len(ans)
        for i in range(x, k):
            ans.append(None)
        return ans