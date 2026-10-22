# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leftCounter = 0
        rightCounter = 0
        prev = None
        curr = head
        right = head

        while right is not None:
            rightCounter += 1
            right = right.next

        position = rightCounter - n

        while True:
            if position != leftCounter:
                leftCounter+=1
                prev = curr
                curr = curr.next
            else:
                next_node = None
                if curr.next is not None:
                    next_node = curr.next

                if prev is not None:
                    curr = prev
                    curr.next = next_node
                else:
                    head = next_node
                
                break
        return head