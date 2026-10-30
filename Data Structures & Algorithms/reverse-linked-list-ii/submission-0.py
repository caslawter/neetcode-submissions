# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = None
        curr = head

        previousLeft = dummy

        for i in range(abs(left) - 1):
            previousLeft = curr
            curr = curr.next

        for i in range(abs(right) - abs(left) + 1):
            tempNext = curr.next
            curr.next = prev
            prev = curr
            curr = tempNext

        previousLeft.next.next = curr
        previousLeft.next = prev
        return dummy.next