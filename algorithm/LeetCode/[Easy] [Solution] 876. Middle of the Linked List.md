876. Middle of the Linked List

Given a non-empty, singly linked list with head node `head`, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

 

**Example 1:**
```
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
```

**Example 2:**
```
Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
```

**Note:**

* The number of nodes in the given list will be between `1` and `100`.

# Solution
---
## Approach 1: Output to Array
**Intuition and Algorithm**

Put every node into an array `A` in order. Then the middle node is just `A[A.length // 2]`, since we can retrieve each node by index.

```python
class Solution(object):
    def middleNode(self, head):
        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A) / 2]
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the number of nodes in the given list.

* Space Complexity: $O(N)$, the space used by `A`.

## Approach 2: Fast and Slow Pointer
**Intuition and Algorithm**

When traversing the list with a pointer `slow`, make another pointer `fast` that traverses twice as fast. When `fast` reaches the end of the list, `slow` must be in the middle.

```python
class Solution(object):
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the number of nodes in the given list.

* Space Complexity: $O(1)$, the space used by slow and fast.

# Submissions
---
**Solution 1: (Fast and Slow Pointer, Linked List)**
```
Runtime: 36 ms
Memory Usage: 12.8 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
```