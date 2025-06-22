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

**Solution 2: (Linked List)**
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

**Solution 3: (Linked List, Stack)**
```
Runtime: 27 ms
Memory: 73.7 MB
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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        stack<int> stk1, stk2;
        while (l1) {
            stk1.push(l1->val);
            l1 = l1->next;
        }
        while (l2) {
            stk2.push(l2->val);
            l2 = l2->next;
        }
        int num1, num2, carry = 0;
        ListNode *cur = nullptr, *pre;
        while (!stk1.empty() || !stk2.empty() || carry) {
            num1 = 0;
            if (!stk1.empty()) {
                num1 = stk1.top();
                stk1.pop();
            }
            num2 = 0;
            if (!stk2.empty())  {
                num2 = stk2.top();
                stk2.pop();
            }
            pre = new ListNode((num1 + num2 + carry)%10);
            carry = (num1 + num2 + carry)/10;
            pre->next = cur;
            cur = pre;          
        }
        return cur;
    }
};
```

**Solution 4: (Linked List)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 76.74 MB, Beats 92.36%
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
    ListNode *reverse(ListNode *node) {
        ListNode *pre = nullptr, *cur = node, *ncur;
        while (cur) {
            ncur = cur->next;
            cur->next = pre;
            pre = cur;
            cur = ncur;
        }
        return pre;
    }
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *nl1, *nl2, *dummy = new ListNode(), *pre;
        int p = 0, a;
        nl1 = reverse(l1);
        nl2 = reverse(l2);
        pre = dummy;
        while (nl1 || nl2 || p) {
            a = (nl1 ? nl1->val : 0) + (nl2 ? nl2->val : 0) + p;
            pre->next = new ListNode(a%10);
            pre = pre->next;
            p = a/10;
            nl1 = nl1 ? nl1->next : nullptr;
            nl2 = nl2 ? nl2->next : nullptr;

        }
        return reverse(dummy->next);
    }
};
```
