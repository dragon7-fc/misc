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