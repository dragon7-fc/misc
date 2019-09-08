82. Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

**Example 1:**
```
Input: 1->2->3->3->4->4->5
Output: 1->2->5
```

**Example 2:**
```
Input: 1->1->1->2->3
Output: 2->3
```

Solution: 44 ms, 13.8 MB
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        if not head:
            return None
        prev, cur, nxt = dummy, head, head.next
        lock = False
        while cur and nxt:
            if cur.val != nxt.val and not lock:
                prev.next = cur
                prev = cur
            elif cur.val != nxt.val and lock:
                lock = False
            else:
                lock = True
            cur = cur.next
            nxt = cur.next
            
        if not lock:
            prev.next = cur
        else:
            prev.next = None
            
        return dummy.next
```