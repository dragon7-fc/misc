2807. Insert Greatest Common Divisors in Linked List

Given the head of a linked list `head`, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the **greatest common divisor** of them.

Return the linked list after insertion.

The **greatest common divisor** of two numbers is the largest positive integer that evenly divides both numbers.

 

**Example 1:**

![2807_ex1_copy.png](img/2807_ex1_copy.png)
```
Input: head = [18,6,10,3]
Output: [18,6,6,2,10,1,3]
Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes (nodes in blue are the inserted nodes).
- We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.
- We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.
- We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.
There are no more adjacent nodes, so we return the linked list.
```

**Example 2:**

![2807_ex2_copy1.png](img/2807_ex2_copy1.png)
```
Input: head = [7]
Output: [7]
Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes.
There are no pairs of adjacent nodes, so we return the initial linked list.
```

**Constraints:**

* The number of nodes in the list is in the range `[1, 5000]`.
* `1 <= Node.val <= 1000`

# Submissions
---
**Solution 1: (Linked List)**
```
Runtime: 93 ms
Memory: 21.2 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur.next:
            node = ListNode(gcd(cur.val, cur.next.val))
            node.next = cur.next
            nxt = cur.next
            cur.next = node
            cur = nxt
        return head
```

**Solution 2: (Linked List)**
```
Runtime: 40 ms
Memory: 35.60 MB
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
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        ListNode *cur = head->next, *pre = head, *node;
        while (cur) {
            node = new ListNode(gcd(cur->val, pre->val));
            pre->next = node;
            node->next = cur;
            pre = cur;
            cur = cur->next;
        }
        return head;
    }
};
```
