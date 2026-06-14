# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ptr1 = head
        prt2 = None
        length = 1
    
        curr = head
        while curr and curr.next:
            length += 1
            curr = curr.next
        # print(length)
        half = length // 2
        curr = head
        for _ in range(half):
            curr = curr.next
        

        
        # reverse the second half
        ptr2 = curr
        prev = None
        while ptr2:
            temp = ptr2.next
            ptr2.next = prev
            prev = ptr2
            ptr2 = temp
        # print(prev)
            
        ptr2 = prev
        max_summ = 0
        while ptr1 and ptr2:
            # print(ptr1.val, ptr2.val)
            max_summ = max(max_summ, ptr1.val + ptr2.val)
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        return max_summ