25. Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

**Example:**

Given this linked list: `1->2->3->4->5`

For k = 2, you should return: `2->1->4->3->5`

For k = 3, you should return: `3->2->1->4->5`

**Note:**
* Only constant extra memory is allowed.
* You may not alter the values in the list's nodes, only nodes itself may be changed.

# Submissions
---
**Solution 1: (Recursion)**
```
Runtime: 68 ms
Memory Usage: 15.3 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseLinkedList(self, head, k):
        
        # Reverse k nodes of the given linked list.
        # This function assumes that the list contains 
        # atleast k nodes.
        new_head, ptr = None, head
        while k:
            
            # Keep track of the next node to process in the
            # original list
            next_node = ptr.next
            
            # Insert the node pointed to by "ptr"
            # at the beginning of the reversed list
            ptr.next = new_head
            new_head = ptr
            
            # Move on to the next node
            ptr = next_node
            
            # Decrement the count of nodes to be reversed by 1
            k -= 1
        
        # Return the head of the reversed list
        return new_head
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        count = 0
        ptr = head
        
        # First, see if there are atleast k nodes
        # left in the linked list.
        while count < k and ptr:
            ptr = ptr.next
            count += 1
        
        # If we have k nodes, then we reverse them
        if count == k: 
            
            # Reverse the first k nodes of the list and
            # get the reversed list's head.
            reversedHead = self.reverseLinkedList(head, k)
            
            # Now recurse on the remaining linked list. Since
            # our recursion returns the head of the overall processed
            # list, we use that and the "original" head of the "k" nodes
            # to re-wire the connections.
            head.next = self.reverseKGroup(ptr, k)
            return reversedHead
        return head
```

**Solution 2: (Iterative O(1) space)**
```
Runtime: 52 ms
Memory Usage: 15.3 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = prev = start = end = ListNode(-1)
        dummy.next = head
        cur = head
        cnt = k
        while end:
            end = end.next
            cnt -= 1
            if cnt == -1:
                while cur != end:
                    nxt = cur.next
                    cur.next = prev
                    prev = cur
                    cur = nxt
                cnt = k-1
                start.next.next = end
                start_nxt = start.next
                start.next = prev
                start = start_nxt
        
        return dummy.next
```

**Solution 3: (Linked List, Stack)**
```
Runtime: 52 ms
Memory Usage: 14.7 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        pointer = head
        stack_pointer = head
        stack = []
        while 1:
            while stack_pointer and len(stack) < k:
                stack.append(stack_pointer.val)
                stack_pointer = stack_pointer.next
            if len(stack) < k:
                return head
            else:
                while len(stack) > 0:
                    pointer.val = stack.pop()
                    pointer = pointer.next
```

**Solution 4: (Recursion)**
```
Runtime: 4 ms
Memory Usage: 7.3 MB
```
```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseKGroup(struct ListNode* head, int k){
    struct ListNode *cur = head, *prev, *nxt;
    int cnt = k;
    while (cnt > 0 && cur) {
        cur = cur->next;
        cnt -= 1;
    }
    if (cnt > 0) {
        return head;
    }
    prev = head;
    cur = head->next;
    cnt = k - 1;
    while (cnt > 0) {
        nxt = cur->next;
        cur->next = prev;
        prev = cur;
        cur = nxt;
        cnt -= 1;
    }
    head->next = reverseKGroup(cur, k);
    return prev;
}
```

**Solution 5: (DFS)**
```
Runtime: 59 ms
Memory: 15.2 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def dfs(node, r):
            cur = node
            while cur and r > 0:
                cur = cur.next
                r -= 1
            if r == 0:
                pre = None
                cur = node
                r = k
                while r > 0:
                    nxt = cur.next
                    cur.next = pre
                    pre = cur
                    cur = nxt
                    r -= 1
                node.next = dfs(cur, k)
                return pre
            else:
                return node  
            
        return dfs(head, k)
```

**Solution 6: (DFS)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 16.46 MB, Beats 70.74%
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
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode *cur = head, *pre, *ncur;
        int ck = 0;
        while (cur && ck < k) {
            cur = cur->next;
            ck += 1;
        }
        if (ck < k) {
            return head;
        }
        pre = head;
        cur = pre->next;
        ck = 1;
        while (ck < k) {
            ncur = cur->next;
            cur->next = pre;
            pre = cur;
            cur = ncur;
            ck += 1;
        }
        head->next = reverseKGroup(cur, k);
        return pre;
    }
};
```

**Solution 7: (iterative)**

ck       1    2    1
    d -> 1 -> 2 -> 3 -> 4 -> 5
              ^c
              ^p   ^c   ^nc
           <-        <-
         ^ed       ^ed
    ^st  ^st       ^st

```
Runtime: 0 ms, Beats 100.00%
Memory: 16.36 MB, Beats 95.85%
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
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode *dummy = new ListNode(), *pre, *cur = head, *st, *ncur, *ed;
        int ck;
        dummy->next = head;
        st = dummy;
        while (cur) {
            ck = 1;
            pre = cur;
            while (ck < k && cur->next) {
                ck += 1;
                cur = cur->next;
            }
            if (ck < k) {
                cur = pre;
                break;
            }
            ed = pre;
            cur = pre->next;
            ck = 1;
            while (ck < k) {
                ncur = cur->next;
                cur->next = pre;
                pre = cur;
                cur = ncur;
                ck += 1;
            }
            st->next = pre;
            st = ed;
        }
        st->next = cur;
        return dummy->next;
    }
};
```
