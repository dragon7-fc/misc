203. Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

**Example:**
```
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
```

# Submissions
---
**Solution 1: (Linked List)**
```
Runtime: 76 ms
Memory Usage: 16.8 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        tmp = dummy
        while dummy.next:
            if dummy.next.val == val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
            
        return tmp.next
```

**Solution 2: (Linked List)**
```
Runtime: 36 ms
Memory Usage: 13.5 MB
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
    ListNode* removeElements(ListNode* head, int val) {
        if(!head)return head;   // return if null
        while(head && head->val == val) head = head->next;   // Set head as the first valid node
        ListNode* trav = head;
        ListNode* temp = NULL;
        while(trav){
            temp = trav;   // store the current node
            while(trav->next && trav->next->val == val){   // Iterate till the last  non valid node
                trav = trav->next;  
            }
            temp->next = trav->next;  // set the next pointer to the first next valid node
            trav=trav->next;
        }
        return head;
 
    }
};
```