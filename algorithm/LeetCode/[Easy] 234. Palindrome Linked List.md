234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

**Example 1:**
```
Input: 1->2
Output: false
```

**Example 2:**
```
Input: 1->2->2->1
Output: true
```

**Follow up:**

* Could you do it in O(n) time and O(1) space?

# Submissions
---
**Solution 1: (Two Pointers)**
```
Runtime: 60 ms
Memory Usage: 22.7 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        
        slow = fast = head
        prev = None
        
        #Reverse the list until it's mid point
        
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
                
        if fast and not fast.next:
            slow = slow.next
        
        while prev and slow:
            if prev.val != slow.val:
                return False
            prev = prev.next
            slow = slow.next
            
        return True
```

**Solution 2: (Two Pointers)**
```
Runtime: 120 ms
Memory Usage: 41.5 MB
```
```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


bool isPalindrome(struct ListNode* head){
    if (!head || !head->next)
        return true;
    struct ListNode *slow, *fast, *prev, *tmp;
    slow = fast = head;
    prev = NULL;
    while (fast && fast->next) {
        fast = fast->next->next;
        tmp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = tmp;
    }
    if (fast && !fast->next)
        slow = slow->next;
    while (prev && slow) {
        if (prev->val != slow->val)
            return false;
        prev = prev->next;
        slow = slow->next;
    }
    return true;
}
```

**Solution 3: (Two Pointers)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 114.06 MB, Beats 99.44%
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
    bool isPalindrome(ListNode* head) {
        ListNode *pre = nullptr, *slow = head, *ncur, *fast = head;
        while (fast && fast->next) {
            fast = fast->next->next;
            ncur = slow->next;
            slow->next = pre;
            pre = slow;
            slow = ncur;
        }
        if (fast) {
            slow = slow->next;
        }
        while (slow != nullptr) {
            if (pre->val != slow->val) {
                return false;
            }
            slow = slow->next;
            pre = pre->next;
        }
        return true;
    }
};
```
