""" 
Linked List Cycle

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


""" Solution1: 60 ms """
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        while head:
            if head.val == sys.maxint:
                return True
            head.val = sys.maxint
            head = head.next
        return False


""" Solution2: 44 ms """
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        walker = head
        runner = head
        while walker.next and runner.next and runner.next.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                return True
        return False