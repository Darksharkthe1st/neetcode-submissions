# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Curr node + next node, then carry to the next
        # I'll assume matching lengths for now
        current = 0
        
        current += l1.val
        current += l2.val
        
        l1 = l1.next
        l2 = l2.next

        building = ListNode(val=-1, next = None)
        head = building
        prev = head

        while l1 and l2:
            current += l1.val * 10
            current += l2.val * 10

            # print(current, l1.val, l2.val)

            l1 = l1.next
            l2 = l2.next

            building.val = current % 10
            current //= 10
            prev = building
            building.next = ListNode(val=-1, next = None)
            building = building.next
        
        while l1:
            current += l1.val * 10

            # print(current, l1.val)

            l1 = l1.next

            building.val = current % 10
            current //= 10
            prev = building
            building.next = ListNode(val=-1, next = None)
            building = building.next
        
        while l2:
            current += l2.val * 10

            # print(current, l2.val)

            l2 = l2.next

            building.val = current % 10
            current //= 10
            prev = building
            building.next = ListNode(val=-1, next = None)
            building = building.next

        # print(current)
        building.val = current % 10
        # print(building.val)
        # print(head.val)
        current //= 10
        if current > 0:
            building.next = ListNode(val=-1, next = None)
            building.next.val = current
        return head



