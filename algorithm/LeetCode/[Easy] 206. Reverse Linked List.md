206. Reverse Linked List

Reverse a singly linked list.

**Example:**
```
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```
**Follow up:**

* A linked list can be reversed either iteratively or recursively. Could you implement both?

# Submissions
---
**Solution 1: (Iterative, Linked List)**
```
Runtime: 40 ms
Memory Usage: N/A
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev
```

**Solution 2: (Recursive, Linked List)**
```
Runtime: 48 ms
Memory Usage: N/A
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
```