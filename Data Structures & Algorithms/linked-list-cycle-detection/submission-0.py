# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast is not None and slow is not None :

            slow = slow.next
            fast = fast.next

            if fast is not None and fast.next is not None:
                fast = fast.next
            else:
                break

            if slow.val == fast.val:
                return True

        return False