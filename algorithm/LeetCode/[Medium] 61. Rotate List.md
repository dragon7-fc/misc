61. Rotate List

Given a linked list, rotate the list to the right by `k` places, where `k` is non-negative.

**Example 1:**
```
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
```

**Example 2:**
```
Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
```

# Sobmissions
---
**Solution 1: (Array, Two Pointers, Linked List)**
```
Runtime: 44 ms
Memory Usage: 13.7 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        circle = []
        length = 0
        dummy = ListNode(0)
        dummy.next = head
        prev, cur = dummy, head
        while cur: 
            length += 1
            circle.append(cur)
            prev = cur
            cur = cur.next
            
        prev.next = head
        
        if length:
            shift = k%length
            circle[-shift-1].next = None     
            return circle[-shift]
        else:
            return None
```

**Solution 2: (Linked List)**
```
Runtime: 32 ms
Memory Usage: 14.1 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        n = 0
        while dummy.next:
            dummy = dummy.next
            n += 1
        if n == 0: return None
        r = n - k%n
        dummy.next = head
        while r > 0:
            dummy = dummy.next
            r -= 1
        nh = dummy.next
        dummy.next = None
        return nh
```

**Solution 3: (Linked List)**
```
Runtime: 6 ms
Memory Usage: 11.7 MB
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
    ListNode* rotateRight(ListNode* head, int k) {
        ListNode *dummy = new ListNode(), *nh;
        int n = 0, r;
        dummy->next = head;
        while (dummy->next) {
            dummy = dummy->next;
            n += 1;
        }
        if (!n)
            return nullptr;
        r = n - k%n;
        dummy->next = head;
        while (r) {
            dummy = dummy->next;
            r -= 1;
        }
        nh = dummy->next;
        dummy->next = nullptr;
        return nh;
    }
};
```
