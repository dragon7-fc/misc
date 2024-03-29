1721. Swapping Nodes in a Linked List

You are given the head of a linked list, and an integer `k`.

Return the head of the linked list after **swapping** the values of the kth node from the beginning and the `k`th node from the end (the list is **1-indexed**).

 

**Example 1:**

![1721_linked1.jpg](img/1721_linked1.jpg)
```
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
```

**Example 2:**
```
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
```

**Example 3:**
```
Input: head = [1], k = 1
Output: [1]
```

**Example 4:**
```
Input: head = [1,2], k = 1
Output: [2,1]
```

**Example 5:**
```
Input: head = [1,2,3], k = 2
Output: [1,2,3]
```

**Constraints:**

* The number of nodes in the list is `n`.
* `1 <= k <= n <= 10^5`
* `0 <= Node.val <= 100`

# Submissions
---
**Solution 1: (Linked List, Two Pointers)**
```
Runtime: 1144 ms
Memory Usage: 48.9 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        walker = runner = head
        for _ in range(k - 1):
            runner = runner.next
        first, runner = runner, runner.next
        while runner:
            walker = walker.next
            runner = runner.next
        walker.val, first.val = first.val, walker.val
        return head
```

**Solution 2: (Linked List, Two Pointers)**
```
Runtime: 755 ms
Memory: 180.1 MB
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
    ListNode* swapNodes(ListNode* head, int k) {
        ListNode *fast = head, *slow = head, *cur;
        for (int i = 1; i < k; i ++) {
            fast = fast->next;
        }
        cur = fast;
        while (fast->next) {
            fast = fast->next;
            slow = slow->next;
        }
        swap(cur->val, slow->val);
        return head;
    }
};
```
