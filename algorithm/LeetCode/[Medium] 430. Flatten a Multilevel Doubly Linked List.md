430. Flatten a Multilevel Doubly Linked List

You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

**Example 1:**
```
Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation:
```

The multilevel linked list in the input is as follows:

![multilevellinkedlist](img/430_multilevellinkedlist.png)

After flattening the multilevel linked list it becomes:

![multilevellinkedlistflattened](img/430_multilevellinkedlistflattened.png)

**Example 2:**
```
Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:

The input multilevel linked list is as follows:

  1---2---NULL
  |
  3---NULL
```

**Example 3:**
```
Input: head = []
Output: []
```

**How multilevel linked list is represented in test case:**

We use the multilevel linked list from Example 1 above:

```
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
```
The serialization of each level is as follows:
```
[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
```
To serialize all levels together we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:
```
[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]
```
Merging the serialization of each level and removing trailing nulls we obtain:
```
[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
```

**Constraints:**

* Number of Nodes will not exceed `1000`.
* `1 <= Node.val <= 10^5`

# Submissions
---
**Solution 1: (Iterative)**
```
Runtime: 900 ms
Memory Usage: 335.8 MB
```
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        node = head
        children = []
        prev = None
        while node:
            node.prev = prev
            if node.child:
                if node.next:
                    children.append(node.next)
                node.next = node.child
                node.child = None
                prev = node
                node = node.next
            elif node.next:
                prev = node
                node = node.next
            else:
                if children:
                    node.next = children.pop()
                    prev = node
                    node = node.next
                else:
                    prev = node    
                    node=node.next
        return head

```

**Solution 2: (Recursive)**
```
Runtime: 956 ms
Memory Usage: 335.7 MB
```
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        p = head
        while p != None and p.child == None:
            p = p.next
        
        if p == None:
            return head
        down = self.flatten(p.child)
        right = self.flatten(p.next)
        p.next = down
        down.prev = p
        p.child = None
        while p.next != None:
            p = p.next
        
        p.next = right
        if right != None:
            right.prev = p
        
        return head

```