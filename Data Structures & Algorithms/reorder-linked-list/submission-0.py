# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        firstHalf, secondHalf = self.getMiddle(head)
        reverse = self.reverseLinkList(secondHalf)
        tail = head
        count = 0


        left = firstHalf.next
        right = reverse

        while left and right:
            if count % 2 == 1:
                tail.next = left
                tail = tail.next
                left = left.next
            else:
                tail.next = right
                tail = tail.next
                right = right.next
                
            count += 1
        tail.next = left if left else right


    def getMiddle(self, head):
        slow = head
        fast = head
        prev = None
        while slow and fast:
            prev = slow
            slow = slow.next
            fast = fast.next

            if fast:
                fast = fast.next
        prev.next = None
        return [head, slow]

    def reverseLinkList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

