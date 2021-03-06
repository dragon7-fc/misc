142. Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return `null`.

To represent a cycle in the given linked list, we use an integer `pos` which represents the position (`0`-indexed) in the linked list where tail connects to. If `pos` is `-1`, then there is no cycle in the linked list.

**Note:** Do not modify the linked list.

**Example 1:**
```
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```
![142_circularlinkedlist](img/142_circularlinkedlist.png)

**Example 2:**
```
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
```
![142_circularlinkedlist_test2](img/142_circularlinkedlist_test2.png)

**Example 3:**
```
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
```
![142_circularlinkedlist_test3](img/142_circularlinkedlist_test3.png)

**Follow-up:**
Can you solve it without using extra space?


Follow-up:
Can you solve it without using extra space?

# Submissions
---
**Solution 1: (Linked List)**
```
Runtime: 44 ms
Memory Usage: 15.8 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next: 
            return
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow: 
                break
        if fast != slow: 
            return
        start = head
        meet = slow
        while meet != start:
            meet = meet.next
            start = start.next
            
        return start
```