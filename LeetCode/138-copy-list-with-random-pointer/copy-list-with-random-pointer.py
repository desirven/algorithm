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
        old_new = {}
        current = head
        while current:
            old_new[current] = Node(current.val)
            current = current.next
        for old, new in old_new.items():
            new.next = old_new.get(old.next, None)
            new.random = old_new.get(old.random, None)
        return old_new.get(head, None)