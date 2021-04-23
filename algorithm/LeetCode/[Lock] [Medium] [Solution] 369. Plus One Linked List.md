369. Plus One Linked List

Given a non-negative integer represented as a linked list of digits, plus one to the integer.

The digits are stored such that the most significant digit is at the `head` of the list.

 

**Example 1:**
```
Input: head = [1,2,3]
Output: [1,2,4]
```

**Example 2:**
```
Input: head = [0]
Output: [1]
```

**Constraints:**

* The number of nodes in the linked list is in the range `[1, 100]`.
* `0 <= Node.val <= 9`
* The number represented by the linked list does not contain leading zeros except for the zero itself. 

# Submissions
---
**Solution 1: (Sentinel Head + Textbook Addition)**
```
Runtime: 32 ms
Memory Usage: 14.2 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        # sentinel head
        sentinel = ListNode(0)
        sentinel.next = head
        not_nine = sentinel

        # find the rightmost not-nine digit
        while head:
            if head.val != 9:
                not_nine = head
            head = head.next

        # increase this rightmost not-nine digit by 1
        not_nine.val += 1
        not_nine = not_nine.next

        # set all the following nines to zeros
        while not_nine:
            not_nine.val = 0
            not_nine = not_nine.next

        return sentinel if sentinel.val else sentinel.next
```

**Solution 2: (DFS)**
```
Runtime: 32 ms
Memory Usage: 14.4 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        def dfs(node):
            if not node.next:
                carry, node.val = divmod(node.val+1, 10)
                return carry
            carry, node.val = divmod(node.val+dfs(node.next), 10)
            return carry
        
        carry = dfs(head)
        if carry:
            node = ListNode(carry)
            node.next = head
            return node
        else:
            return head
```