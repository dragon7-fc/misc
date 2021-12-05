24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

You may **not** modify the values in the list's nodes, only nodes itself may be changed.

 

**Example:**
```
Given 1->2->3->4, you should return the list as 2->1->4->3.
```

# Submissions
---
**Solution 1: (Iterative, Linked List)**
```
Runtime: 36 ms
Memory Usage: 13.9 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            dummy = ListNode(0)
            dummy.next = head
            ans = dummy.next.next
            ptr = dummy
            while head and head.next:
                next_head = head.next.next
                head.next.next = head
                ptr.next = head.next
                ptr = head
                head = next_head
                
            if not head:
                ptr.next = None
            elif not head.next:
                ptr.next =head
            
            return ans
        else:
            return head
```

**Solution 2: (Recursive, Linked List)**
```
Runtime: 32 ms
Memory Usage: 13.8 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        first = head
        sec = head.next
        first.next = self.swapPairs(sec.next)
        sec.next = first
        return sec
```

**Solution 3: (Recursive, Linked List)**
```
Runtime: 0 ms
Memory Usage: 5.8 MB
```
```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* swapPairs(struct ListNode* head){
    if (!head || !head->next)
        return head;
    struct ListNode *reverse_node, *prev, *cur;
    reverse_node = swapPairs(head->next->next);
    prev = head;
    cur = prev->next;
    cur->next = prev;
    prev->next = reverse_node;
    return cur;
}
```
