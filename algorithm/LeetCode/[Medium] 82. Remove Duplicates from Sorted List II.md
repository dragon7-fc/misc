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

# Sobmissions
---
**Solution 1: (Three Pointers, Linked List)**
```
Runtime: 40 ms
Memory Usage: 12.8 MB
```
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

**Solution 2: (Greedy)**
```
Runtime: 44 ms
Memory Usage: 14.2 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        s = []
        dup = 0
        while head:
            if not s:
                s += [head]
            else:
                if s[-1].val == head.val:
                    dup = 1
                elif s[-1].val < head.val:
                    if dup:
                        s.pop()
                    dup = 0
                    s += [head]
                    if len(s) >= 2:
                        s[-2].next = s[-1]
            head = head.next
            if not head and dup:
                s.pop()
                if s:
                    s[-1].next = None
                
        return s[0] if s else None
```

**Solution 3: (Linked List)**
```
Runtime: 4 ms
Memory Usage: 6.3 MB
```
```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* deleteDuplicates(struct ListNode* head){
    struct ListNode *dummy, *begin, *base, *prev;
    dummy = malloc(sizeof(struct ListNode));
    prev = begin = dummy;
    dummy->next = head;
    while (head) {
        base = prev = head;
        head = head->next;
        while (head) {
            if (head->val != prev->val)
                break;
            prev = head;
            head = head->next;
        }
        if (base == prev)
            begin = prev;
        else;
            begin->next = head;
    }
    return dummy->next;
}
```
