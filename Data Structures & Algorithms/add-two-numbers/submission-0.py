# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        count = 1

        total1 = 0
        total2 = 0

        while l1:
            total1 += l1.val * count
            count *= 10
            l1 = l1.next

        count = 1
        while l2:
            total2 += l2.val * count
            count *= 10
            l2 = l2.next

        num = str(total2 + total1)

        ans = ListNode(0)
        tail = ans
        for i in range(len(num) - 1, -1, -1):
            tail.next = ListNode(int(num[i]))
            tail = tail.next

        return ans.next
