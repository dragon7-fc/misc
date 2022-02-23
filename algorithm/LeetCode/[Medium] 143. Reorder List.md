143. Reorder List

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

**Example 1:**
```
Given 1->2->3->4, reorder it to 1->4->2->3.
```

**Example 2:**
```
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
```
# Sobmissions
---
**Solution 1: (Linked List)**
```
Runtime: 96 ms
Memory Usage: 22.3 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        n = len(nodes)
        middle = n // 2

        for i in range(middle):
            nodes[i].next = nodes[n-1-i]
            nodes[n-1-i].next = nodes[i+1]

        nodes[middle].next = None
```

**Solution 2: (Linked List, Reverse the Second Part of the List and Merge Two Sorted Lists)**
```
Runtime: 100 ms
Memory Usage: 23.3 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return 
        
        # find the middle of linked list [Problem 876]
        # in 1->2->3->4->5->6 find 4 
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            
        # reverse the second part of the list [Problem 206]
        # convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
        # reverse the second half in-place
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next       

        # merge two sorted linked lists [Problem 21]
        # merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
```

**Solution 3: (Linked List, Reverse the Second Part of the List and Merge Two Sorted Lists)**
```
Runtime: 12 ms
Memory Usage: 9.1 MB
```
```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


void reorderList(struct ListNode* head){
    struct ListNode *fast, *slow, *prev, *nxt, *dummy;
    dummy = malloc(sizeof(struct ListNode));
    dummy->next = slow = fast = head;
    while (fast && fast->next) {
        prev = slow;
        slow = slow->next;
        fast = fast->next->next;
    }
    if (fast && !fast->next) {
        prev = slow;
        slow = slow->next;
    }
    prev->next = NULL;
    prev = NULL;
    while (slow) {
        nxt = slow->next;
        slow->next = prev;
        prev = slow;
        slow = nxt;
    }
    slow = prev;
    while (slow) {
        nxt = head->next;
        prev = slow->next;
        head->next = slow;
        slow->next = nxt;
        slow = prev;
        head = nxt;
    }
    return dummy->next;
}
```

**Solution 4: (Linked List)**
```
Runtime: 46 ms
Memory Usage: 18.8 MB
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
    void reorderList(ListNode* head) {
        vector<ListNode*> nodes;
        ListNode *cur = head;
        while (cur) {
            nodes.push_back(cur);
            cur = cur->next;
        }
        int n = nodes.size();
        int middle = n/2;
        for (int i = 0; i < middle; i ++) {
            nodes[i]->next = nodes[n-1-i];
            nodes[n-1-i]->next = nodes[i+1];
        }
        nodes[middle]->next = nullptr;
    }
};
```

**Solution 5: (Linked List, Reverse the Second Part of the List and Merge Two Sorted Lists)**
```
Runtime: 68 ms
Memory Usage: 17.7 MB
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
    void reorderList(ListNode* head) {
        if (!head)
            return;
        ListNode *slow = head, *fast = head;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode *prev = nullptr, *curr = slow, *tmp;
        while (curr) {
            tmp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = tmp;
        }
        ListNode *first = head, *second = prev, *first_tmp, *second_tmp;
        while (second->next) {
            first_tmp = first->next;
            first->next = second;
            first = first_tmp;
            second_tmp = second->next;
            second->next = first;
            second = second_tmp;
        }
    }
};
```
