2181. Merge Nodes in Between Zeros

You are given the `head` of a linked list, which contains a series of integers **separated** by `0`'s. The **beginning** and **end** of the linked list will have `Node.val == 0`.

For **every** two consecutive `0`'s, **merge** all the nodes lying in between them into a single node whose value is the **sum** of all the merged nodes. The modified list should not contain any `0`'s.

Return the `head` of the modified linked list.

 

**Example 1:**

![2181_ex1-1.png](img/2181_ex1-1.png)
```
Input: head = [0,3,1,0,4,5,2,0]
Output: [4,11]
Explanation: 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 3 + 1 = 4.
- The sum of the nodes marked in red: 4 + 5 + 2 = 11.
```

**Example 2:**

![2181_ex2-1.png](img/2181_ex2-1.png)
```
Input: head = [0,1,0,3,0,2,2,0]
Output: [1,3,4]
Explanation: 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 1 = 1.
- The sum of the nodes marked in red: 3 = 3.
- The sum of the nodes marked in yellow: 2 + 2 = 4.
```

Constraints:

* The number of nodes in the list is in the range `[3, 2 * 10^5]`.
* `0 <= Node.val <= 1000`
* There are **no** two consecutive nodes with `Node.val == 0`.
* The **beginning** and **end** of the linked list have `Node.val == 0`.

# Submissions
---
**Solution 1: (Linked List)**
```
Runtime: 4241 ms
Memory Usage: 72.8 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        dummy = prev = ListNode(-math.inf)
        while head and head.next:
            prev.next = head
            head = head.next
            while head and head.val != 0:
                prev.next.val += head.val
                head = head.next
            prev = prev.next
        prev.next = None    
        return dummy.next
```

**Solution 2: (Linked List)**
```
Runtime: 889 ms
Memory Usage: 256.2 MB
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
    ListNode* mergeNodes(ListNode* head) {
        //BASE CASE -> if we have a single zero, simply return null
        if(!head->next) return nullptr;

        //fetch sum from current 0 to next 0
        ListNode* ptr= head->next;
        int sum=0;
        while(ptr->val!=0) sum+= ptr->val, ptr=ptr->next;

        //assign sum on the first node between nodes having value 0.
        head->next->val= sum;

        //call and get the answer and connect the answer to next of head->next
        head->next->next= mergeNodes(ptr);

        //return head->next..=> new head
        return head->next;
    }
};
```
