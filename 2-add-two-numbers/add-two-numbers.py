# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output_head = output_list = ListNode()
        up_flag = 0

        while l1 or l2 or up_flag:
            _sum = up_flag
            if l1:
               _sum += l1.val
               l1 = l1.next
            if l2:
                _sum += l2.val
                l2 = l2.next
            
            if _sum >= 10:
                _sum -= 10
                up_flag = 1
            else:
                up_flag = 0
            
            output_list.next = ListNode(val=_sum)
            output_list = output_list.next

        return output_head.next