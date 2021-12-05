83. Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

**Example 1:**
```
Input: 1->1->2
Output: 1->2
```

**Example 2:**
```
Input: 1->1->2->3->3
Output: 1->2->3
```

# Solution
---
## Approach 1: Straight-Forward Approach
**Algorithm**

This is a simple problem that merely tests your ability to manipulate list node pointers. Because the input list is sorted, we can determine if a node is a duplicate by comparing its value to the node after it in the list. If it is a duplicate, we change the next pointer of the current node so that it skips the next node and points directly to the one after the next node.

```java
public ListNode deleteDuplicates(ListNode head) {
    ListNode current = head;
    while (current != null && current.next != null) {
        if (current.next.val == current.val) {
            current.next = current.next.next;
        } else {
            current = current.next;
        }
    }
    return head;
}
```

**Complexity Analysis**

* Time complexity : $O(n)$. Because each node in the list is checked exactly once to determine if it is a duplicate or not, the total run time is $O(n)$, where $n$ is the number of nodes in the list.

* Space complexity : $O(1)$. No additional space is used.

**Correctness**

We can prove the correctness of this code by defining a loop invariant. A loop invariant is condition that is true before and after every iteration of the loop. In this case, a loop invariant that helps us prove correctness is this:

> All nodes in the list up to the pointer current do not contain duplicate elements.

We can prove that this condition is indeed a loop invariant by induction. Before going into the loop, `current` points to the head of the list. Therefore, the part of the list up to `current` contains only the head. And so it can not contain any duplicate elements. Now suppose `current` is now pointing to some node in the list (but not the last element), and the part of the list up to `current` contains no duplicate elements. After another loop iteration, one of two things happen.

* `current.next` was a duplicate of current. In this case, the duplicate node at `current.next` is deleted, and `current` stays pointing to the same node as before. Therefore, the condition still holds; there are still no duplicates up to current.

* `current.next` was not a duplicate of current (and, because the list is sorted, current.next is also not a duplicate of any other element appearing before current). In this case, `current` moves forward one step to point to `current.next`. Therefore, the condition still holds; there are no duplicates up to current.

At the last iteration of the loop, `current` must point to the last element, because afterwards, `current.next = null`. Therefore, after the loop ends, all elements up to the last element do not contain duplicates.

# Submissions
---
**Solution 1: (Linked List)*
```
Runtime: 32 ms
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
        current = head
        while current and current.next:
            if current.next.val == current.val:
                current.next = current.next.next;
            else:
                current = current.next 
            
        return head
```

**Solution 2: (Linked List)*
```
Runtime: 0 ms
Memory Usage: 6.4 MB
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
    struct ListNode *dummy, *base;
    dummy = malloc(sizeof(struct ListNode));
    dummy->next = head;
    while (head) {
        base = head;
        while (head) {
            if (head->val != base->val)
                break;
            head = head->next;
        }
        base->next = head;
        base = base->next;
    }
    return dummy->next;
}
```
