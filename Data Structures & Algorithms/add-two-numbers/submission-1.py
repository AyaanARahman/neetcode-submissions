# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # Dummy node lets us build the result list without
        # worrying about handling the first node separately.
        dummy = ListNode(0)
        start = dummy

        # Carry stores the extra 1 when a digit sum >= 10.
        carry = 0

        # Keep going while either list has digits OR
        # we still have a carry to add.
        while l1 or l2 or carry:

            # If l1 still has a node, use its digit.
            # Otherwise, treat the missing digit as 0.
            if l1:
                val1 = l1.val
            else:
                val1 = 0
            
            if l2:
                val2 = l2.val
            else:
                val2 = 0
            
            resVal = val1 + val2 + carry

            # Extract the carry for the NEXT digit.
            # Example: 14 // 10 = 1
            carry = resVal // 10

            resVal = resVal % 10

            start.next = ListNode(resVal)
            start = start.next

            if l1:
                l1 = l1.next
            else:
                l1 = None
            
            if l2:
                l2 = l2.next
            else:
                l2 = None
        return dummy.next
        