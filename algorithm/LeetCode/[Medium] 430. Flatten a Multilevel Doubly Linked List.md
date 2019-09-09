430. Flatten a Multilevel Doubly Linked List

You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

**Example:**
```
Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL
```

**Explanation for the above example:**

Given the following multilevel doubly linked list:

![multilevellinkedlist](img/430_multilevellinkedlist.png)

We should return the following flattened doubly linked list:

![multilevellinkedlistflattened](img/430_multilevellinkedlistflattened.png)

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