# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head

        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        # print(arr)
        n = len(arr)
        for i in range(1, n):
            temp = arr[i]
            j = i-1
            while j >= 0 and arr[j] > temp:
                arr[j+1] = arr[j]
                j -= 1
            arr[j +1] = temp

        # print(arr)
        head = ListNode(arr[0])
        curr = head
        for i in range(1, n):
            curr.next = ListNode(arr[i])
            curr = curr.next
        # print(head)
        return head