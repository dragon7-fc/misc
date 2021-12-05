206. Reverse Linked List

Reverse a singly linked list.

**Example:**
```
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```
**Follow up:**

* A linked list can be reversed either iteratively or recursively. Could you implement both?

# Submissions
---
**Solution 1: (Iterative, Linked List)**
```
Runtime: 40 ms
Memory Usage: N/A
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev
```

**Solution 2: (Recursive, Linked List)**
```
Runtime: 48 ms
Memory Usage: N/A
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
```

**Solution 3: (Iterative, Linked List)**
```
Runtime: 8 ms
Memory Usage: 8.2 MB
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
    ListNode* reverseList(ListNode* head) {
        ListNode *curr = head,*prev = NULL,*next_node;
        while(curr!=NULL){
            next_node = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next_node;
        }
        return prev;
    }
};
```
**Solution 4: (Recursive, Linked List)**
```
Runtime: 8 ms
Memory Usage: 8.8 MB
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
    ListNode* new_head = NULL;
    
    ListNode* reverse(ListNode* curr){
        if(curr==NULL)
            return curr;
        ListNode* node = reverse(curr->next);
        ListNode* now = new ListNode(curr->val);
        if(node==NULL){
            new_head = now;
        }
        else{
            node->next = now;
        }
        now->next = NULL;
        return now;
    }

    
    ListNode* reverseList(ListNode* head) {
        reverse(head);
        return new_head;
    }
};
```

**Solution 5: (Iterativa, Linked List)**
```
Runtime: 6 ms
Memory Usage: 6.3 MB
```
```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseList(struct ListNode* head){
    struct ListNode *prev, *nxt;
    prev = NULL;
    while (head) {
        nxt = head->next;
        head->next = prev;
        prev = head;
        head = nxt;
    }
    return prev;
}
```

**Solution 6: (Recursive, Linked List)**
```
Runtime: 0 ms
Memory Usage: 6.8 MB
```
```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode *new_head;

struct ListNode* reverse(struct ListNode* node){
    if (!node)
        return node;
    struct ListNode* reverse_node = reverse(node->next);
    if (!reverse_node)
        new_head = node;
    else
        reverse_node->next = node;
    node->next = NULL;
    return node;
}

struct ListNode* reverseList(struct ListNode* head){
    new_head = NULL;
    reverse(head);
    return new_head;
}
```
