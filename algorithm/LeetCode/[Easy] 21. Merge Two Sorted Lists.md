21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

**Example:**
```
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```

# Submissions
---
**Solution 1: (Linked List)**
```
Runtime: 36 ms
Memory Usage: 12.7 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        current = None
        head = None
        while l1 and l2:
            if l1.val <= l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next
            if current == None:
                current = node
                head = current
            else:
                current.next = node
                current = current.next
        if head == None:
            head = l1 or l2
            current = head
        else:
            current.next = l1 or l2
        return head
```

**Solution 2: (Linked List)**
```
Runtime: 4 ms
Memory Usage: 6.1 MB
```
```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    struct ListNode *dummy, *prev;
    prev = dummy = malloc(sizeof(struct ListNode));
    dummy->next = NULL;
    while (list1 && list2) {
        if (list1->val <= list2->val) {
            prev->next = list1;     
            list1 = list1->next;
        } else {
            prev->next = list2;
            list2 = list2->next;
        }
        prev = prev->next;
    }
    if (list1)
        prev->next = list1;
    else if (list2)
        prev->next = list2;
    return dummy->next;
}
```
