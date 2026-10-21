# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        tail = ans

        while list1 or list2:

            if list1 == None:
                tail.next = list2
                tail = tail.next
                list2 = list2.next
                continue
            elif list2 == None:
                tail.next = list1
                tail = tail.next
                list1 = list1.next
                continue

            if list2.val > list1.val:
                tail.next = list1
                tail = tail.next
                list1 = list1.next

            else:
                tail.next = list2
                tail = tail.next
                list2 = list2.next
        
        return ans.next