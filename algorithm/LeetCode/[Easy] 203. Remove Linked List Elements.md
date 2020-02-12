203. Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

**Example:**
```
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
```

# Submissions
---
**Solution 1: (Linked List)**
```
Runtime: 76 ms
Memory Usage: 16.8 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        tmp = dummy
        while dummy.next:
            if dummy.next.val == val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
            
        return tmp.next
```