234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

**Example 1:**
```
Input: 1->2
Output: false
```

**Example 2:**
```
Input: 1->2->2->1
Output: true
```

**Follow up:**

* Could you do it in O(n) time and O(1) space?

# Submissions
---
**Solution 1: (Two Pointers)**
```
Runtime: 60 ms
Memory Usage: 22.7 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        
        slow = fast = head
        prev = None
        
        #Reverse the list until it's mid point
        
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
                
        if fast and not fast.next:
            slow = slow.next
        
        while prev and slow:
            if prev.val != slow.val:
                return False
            prev = prev.next
            slow = slow.next
            
        return True
```