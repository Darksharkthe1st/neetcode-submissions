# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ahead = head
        for i in range(n):
            ahead = ahead.next

        if ahead is None:
            return head.next
        curr = head
        while ahead.next:
            ahead = ahead.next
            curr = curr.next
        
        curr.next = curr.next.next

        return head