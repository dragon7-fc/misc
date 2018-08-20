""" 
Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


""" Solution: 124 ms """
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rev = None
        walker = runner = head
        while runner and runner.next:
            runner = runner.next.next
            rev, rev.next, walker = walker, rev, walker.next
        if runner:
            walker = walker.next
        while rev and rev.val == walker.val:
            walker = walker.next
            rev = rev.next
        return not rev