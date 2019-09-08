203. Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

**Example:**
```
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
```

Solution 1: 88 ms, 17.1 MB
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
        prev = dummy
        while head:
            if head.val == val:
                prev.next = head.next
                head = prev.next
            else:
                prev = head
                head = head.next
            
        return dummy.next
```

Solution 2: 76 ms, 16.8 MB
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