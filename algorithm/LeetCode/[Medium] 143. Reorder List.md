143. Reorder List

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

**Example 1:**
```
Given 1->2->3->4, reorder it to 1->4->2->3.
```

**Example 2:**
```
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
```
# Sobmissions
---
**Solution: 96 ms, 22.3 MB**
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
			
        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        n = len(nodes)
        middle = n // 2

        for i in range(middle):
            nodes[i].next = nodes[n-1-i]
            nodes[n-1-i].next = nodes[i+1]

        nodes[middle].next = None
```