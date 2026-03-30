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

        toNew = {}
        curr = head

        while curr:

            copy = Node(curr.val)

            toNew[curr] = copy
            curr = curr.next

        curr = head

        while curr:
            copy = toNew.get(curr)
            copy.next = toNew.get(curr.next)
            copy.random = toNew.get(curr.random)
            curr = curr.next
        return toNew.get(head)


        