445. Add Two Numbers II

Share
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
**Solution 1: (Stack, Linked List)**
```
Runtime: 76 ms
Memory Usage: 13.9 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = l1
        num1, num2 = 0, 0
        stack = []
        
        while cur:
            num1 = num1*10 + cur.val
            cur = cur.next
            
        cur = l2
        while cur:
            num2 = num2*10 + cur.val
            cur = cur.next
        
        sum_ = num1+num2
        while sum_ >= 10:
            sum_, mod = divmod(sum_, 10)
            stack.append(ListNode(mod))
        stack.append(ListNode(sum_))
        
        if len(stack) >= 2:
            for i in range(len(stack)-1, 0, -1):
                stack[i].next = stack[i-1]
            
        return stack[-1]
```

**Solution 2: (String, Stack, Linked List)**
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