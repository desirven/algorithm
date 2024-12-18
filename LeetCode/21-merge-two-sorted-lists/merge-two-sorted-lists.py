# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res_cur = res_head = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                res_cur.next = list1
                list1 = list1.next
            else:
                res_cur.next = list2
                list2 = list2.next
            
            res_cur = res_cur.next

        if list1:
            res_cur.next = list1
        else:
            res_cur.next = list2
        return res_head.next