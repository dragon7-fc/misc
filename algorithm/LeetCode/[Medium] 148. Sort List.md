148. Sort List

Sort a linked list in O(n log n) time using constant space complexity.

**Example 1:**
```
Input: 4->2->1->3
Output: 1->2->3->4
```

**Example 2:**
```
Input: -1->5->3->4->0
Output: -1->0->3->4->5
```

# Submissions
---
**Solution 1: (Sort, Linked list)**
```
Runtime: 236 ms
Memory Usage: 21.9 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(h1, h2):
            cur = dummy = ListNode(-1)
            while h1 and h2:
                if h1.val < h2.val:
                    cur.next, h1 = h1, h1.next
                else:
                    cur.next, h2 = h2, h2.next
                cur = cur.next
            cur.next = h1 or h2
            return dummy.next
        
        if not head or not head.next: return head
        pres = slow = fast = head
        while fast and fast.next:
            pres = slow
            slow = slow.next
            fast = fast.next.next
        pres.next = None  #cut off in the middle
        first = self.sortList(head)
        second = self.sortList(slow)
        return merge(first, second)
```