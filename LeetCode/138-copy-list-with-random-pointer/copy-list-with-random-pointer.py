"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        cur = head
        while cur:
            cur.next = Node(cur.val, cur.next, cur.random)
            cur = cur.next.next
        
        cur = head.next
        while cur:
            cur.random = getattr(cur.random, 'next', None)
            if cur.next:
                cur = cur.next.next
            else:
                break

        result_head = head.next
        cur = result_head
        while cur.next:
            cur.next = cur.next.next
            cur = cur.next
        return result_head