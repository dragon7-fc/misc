445. Add Two Numbers II

You are given two **non-empty** linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Follow up:**
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

**Example:**
```
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
```

# Submissions
---
**Solution 1: (String, Linked List)**
```
Runtime: 64 ms
Memory Usage: 14.1 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = 0
        while l1 != None:
            cur = cur*10 + l1.val
            l1 = l1.next
        n1 = cur
        cur = 0
        while l2:
            cur = cur*10 + l2.val
            l2 = l2.next
        n2 = cur
        s = list(str(n1+n2))
        dummy = cur = ListNode(-1)
        while s:
            cur.next = ListNode(s[0])
            cur = cur.next
            s.pop(0)
        return dummy.next 
```

**Solution 1: (Linked List)**
```
Runtime: 12 ms
Memory Usage: 7.9 MB
```
```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* reverse(struct ListNode *node) {
    struct ListNode *prev = NULL, *cur = node, *nxt;
    while (cur) {
        nxt = cur->next;
        cur->next = prev;
        prev = cur;
        cur = nxt;
    }
    return prev;
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode *prev = NULL, *cur;
    int sum = 0, carry = 0;
    l1 = reverse(l1);
    l2 = reverse(l2);
    while (l1 || l2 || carry) {
        sum = carry;
        if (l1) {
            sum += l1->val;
            l1 = l1->next;
        }
        if (l2) {
            sum += l2->val;
            l2 = l2->next;
        }
        cur = malloc(sizeof(struct ListNode));
        cur->val = sum % 10;
        cur->next = prev;
        prev = cur;
        carry = sum >= 10 ? 1 : 0;
    }
    return prev;
}
```
