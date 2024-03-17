1171. Remove Zero Sum Consecutive Nodes from Linked List

Given the `head` of a linked list, we repeatedly delete consecutive sequences of nodes that sum to `0` until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

 

(Note that in the examples below, all sequences are serializations of `ListNode` objects.)

**Example 1:**
```
Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
```

**Example 2:**
```
Input: head = [1,2,3,-3,4]
Output: [1,2,4]
```

**Example 3:**
```
Input: head = [1,2,3,-3,-2]
Output: [1]
```

**Constraints:**

* The given linked list will contain between `1` and `1000` nodes.
* Each node in the linked list has `-1000 <= node.val <= 1000`.

# Sobmissions
---
**Solution 1: (Prefix Sum, Linked List)**
```
Runtime: 52 ms
Memory Usage: 14 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        prefix_sum = 0
        seen = {prefix_sum: dummy}
        
        while head:
            prefix_sum += head.val

            # remove elements in zero sum
            if prefix_sum in seen:           
                k, v = seen.popitem()
                while k != prefix_sum:
                    k, v = seen.popitem()
                seen[k] = v
            else:
                # add non zero-sum elements
                seen[prefix_sum] = head
            
            head = head.next
        
        # rebuild the linkedlist
        ret = dummy
        for i, k in enumerate(seen):
            if i > 0:
                ret.next = seen[k]
                ret = ret.next
        
        ret.next = None
        
        return dummy.next
```

**Solution 2: (Prefix Sum, Linked List)**
```
Runtime: 8 ms
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
#define MAX_NODES 1000

struct ListNode* removeZeroSumSublists(struct ListNode* head){
    struct node {
        struct ListNode *curr;
        int sum;
    };
    struct ListNode dummy = {
        .val  = 0,
        .next = head,
    };
    struct node prefixSum[MAX_NODES + 1] = {{0}};
    int sum                              = 0;
    int size                             = 0;
    struct ListNode *curr                = &dummy;
    while (curr) {
        sum                 += curr->val;
        prefixSum[size].sum  = sum;
        prefixSum[size].curr = curr;
        size++;
        curr = curr->next;
    }
    for (int i = 0; i < size; i++) {
        for (int j = size - 1; j > i; j--) {
            if (prefixSum[i].sum == prefixSum[j].sum) {
                prefixSum[i].curr->next = prefixSum[j].curr->next;
                i                       = j;
                break;
            }
        }
    }
    return dummy.next;
}
```

**Solution 3: (Prefix Sum, Linked List, Hash Table)**
```
Runtime: 3 ms
Memory: 14.94 MB
```
```c++
[200~/**
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
    ListNode* removeZeroSumSublists(ListNode* head) {
        unordered_map<int, ListNode*> m;
        ListNode *dummy = new ListNode(0), *cur;
        int pre = 0, nxt;
        dummy->next = head;
        m[0] = dummy;
        while (head) {
            pre += head->val;
            if (m.count(pre)) {
                cur = m[pre]->next;
                nxt = pre + cur->val;
                while (nxt != pre) {
                    m.erase(nxt);
                    cur = cur->next;
                    nxt += cur->val;
                }
                m[pre]->next = cur->next;
            } else {
                m[pre] = head;
            }
            head = head->next;
        }
        return dummy->next;
    }
};
```
