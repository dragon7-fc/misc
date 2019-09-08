725. Split Linked List in Parts

Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.

Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]

**Example 1:**
```
Input: 
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The input and each element of the output are ListNodes, not arrays.
For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null.
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but it's string representation as a ListNode is [].
```

**Example 2:**
```
Input: 
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
```

Note:
* The length of root will be in the range [0, 1000].
* Each value of a node in the input will be an integer in the range [0, 999].
* k will be an integer in the range [1, 50].

Solution 1: 44 ms, 13.8 MB
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        ans = []
        length = 0
        
        cur = root
        while cur:
            length += 1
            cur = cur.next
            
        part_size, remainder = divmod(length, k)
        
        cur = root
        for i in range(k):
            dummy = ListNode(0)
            node = dummy
            for j in range(part_size + (i < remainder)):
                node.next = ListNode(cur.val)
                node = node.next              
                cur = cur.next
                    
            ans.append(dummy.next)
        
        return ans
```

Solution 2: 40 ms, 14 MB
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        ans = []
        length = 0
        
        cur = root
        while cur:
            length += 1
            cur = cur.next
            
        part_size, remainder = divmod(length, k)
        
        cur = root
        for i in range(k):
            head = cur
            for j in range(part_size + (i < remainder) - 1):
                if cur:
                    cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
            
            ans.append(head)
        
        return ans
```
# [Solution] Approach #1: Create New Lists [Accepted]

**Intuition and Algorithm**

If there are $N$ nodes in the linked list root, then there are $N/k$ items in each part, plus the first $N\%k$ parts have an extra item. We can count $N$ with a simple loop.

Now for each part, we have calculated how many nodes that part will have: `width + (i < remainder ? 1 : 0)`. We create a new list and write the part to that list.

Our solution showcases constructs of the form a = b = c. Note that this syntax behaves differently for different

```python
class Solution(object):
    def splitListToParts(self, root, k):
        cur = root
        for N in xrange(1001):
            if not cur: break
            cur = cur.next
        width, remainder = divmod(N, k)

        ans = []
        cur = root
        for i in xrange(k):
            head = write = ListNode(None)
            for j in xrange(width + (i < remainder)):
                write.next = write = ListNode(cur.val)
                if cur: cur = cur.next
            ans.append(head.next)
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N + k)$, where $N$ is the number of nodes in the given list. If $k$ is large, it could still require creating many new empty lists.
* Space Complexity: $O(max(N, k))$, the space used in writing the answer.

# [Solution] Approach #2: Split Input List [Accepted]

**Intuition and Algorithm**

As in Approach #1, we know the size of each part. Instead of creating new lists, we will split the input list directly and return a list of pointers to nodes in the original list as appropriate.

Our solution proceeds similarly. For a part of size L = width + (i < remainder ? 1 : 0), instead of stepping L times, we will step L-1 times, and our final time will also sever the link between the last node from the previous part and the first node from the next part.

```python
class Solution(object):
    def splitListToParts(self, root, k):
        cur = root
        for N in xrange(1001):
            if not cur: break
            cur = cur.next
        width, remainder = divmod(N, k)

        ans = []
        cur = root
        for i in xrange(k):
            head = cur
            for j in xrange(width + (i < remainder) - 1):
                if cur: cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
            ans.append(head)
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N + k)$, where $N$ is the number of nodes in the given list. If $k$ is large, it could still require creating many new empty lists.
* Space Complexity: $O(k)$, the additional space used in writing the answer.
