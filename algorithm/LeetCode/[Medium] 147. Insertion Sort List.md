147. Insertion Sort List

Sort a linked list using insertion sort.

![Example](img/147_Insertion-sort-example-300px.gif)

A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

1. Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
1. At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
1. It repeats until no input elements remain.

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

# Sobmissions
---
**Solution 1: (Linked List)**
```
Runtime: 196 ms
Memory Usage: 14.5 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        while prev.next and prev.next.next:
            # incremental number
            if prev.next.val <= prev.next.next.val:
                prev = prev.next
            else:
                cur = prev.next.next
                prev.next.next = cur.next
                tmp = dummy

                # insert node
                while tmp.next.val <= cur.val:
                    tmp = tmp.next
                cur.next = tmp.next
                tmp.next = cur
        return dummy.next
```

**Solution 2: (Linked List)**
```
Runtime: 8 ms
Memory Usage: 6.9 MB
```
```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* insertionSortList(struct ListNode* head){
    struct ListNode *dummy, *prev, *cur, *tmp;
    dummy = malloc(sizeof(struct ListNode));
    dummy->next = head;
    prev = dummy;
    while (prev->next && prev->next->next) {
        if (prev->next->val <= prev->next->next->val) {
            prev = prev->next;
        } else {
            cur = prev->next->next;
            prev->next->next = cur->next;

            // insert node
            tmp = dummy;
            while (tmp->next->val <= cur->val)
                tmp = tmp->next;
            cur->next = tmp->next;
            tmp->next = cur;
        }
    }
    return dummy->next;
}
```

**Solution 3: (Linked List)**

    4 -> 2 -> 1 -> 3
              ^h

    d -> 2 -> 4
    ^c

```
Runtime: 23 ms, Beats 50.53%
Memory: 15.16 MB, Beats 15.81%
```
```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
        ListNode *dummy = new ListNode(-10000), *pre, *cur, *ncur;
        while (head) {
            cur = dummy;
            while (cur && cur->val < head->val) {
                pre = cur;
                cur = cur->next;
            }
            ncur = new ListNode(head->val);
            pre->next = ncur;
            if (cur) {
                ncur->next = cur;
            }
            head = head->next;
        }
        return dummy->next;
    }
};
```
