138. Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

**Example 1:**

![Example 1](img/138_example1.png)
```
Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
```

Note:

* You must return the copy of the given head as a reference to the cloned list.

# Sobmissions
---
**Solution 1: (Hash Table, Linked List)**
```
Runtime: 44 ms
Memory Usage: 16.3 MB
```
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        copy_dict = {}
        cur = head
        while cur:
            copy_dict[cur] = Node(cur.val, None, None)
            cur = cur.next
            
        cur = head
        while cur:
            if cur.next:
                copy_dict[cur].next = copy_dict[cur.next]
            if cur.random:
                copy_dict[cur].random = copy_dict[cur.random]
            cur = cur.next
        
        return copy_dict[head]
```

**Solution 2: (Hash Table, Linked List)**
```
Runtime: 8 ms
Memory Usage: 11.1 MB
```
```c++
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        Node* newHead = nullptr;
        auto node = head;
        unordered_map<Node*, Node*> old2NewHash;
        
        //copy node
        Node* pre = nullptr;
        while(node) {
            Node* copy = new Node(node->val);
            old2NewHash[node] = copy;
            if(!newHead)
                newHead = copy;
           if(pre)
               pre->next = copy;
            node = node->next;
            pre = copy;
        }
        
        // fill random 
        node = head;
        Node* newNode = newHead;
        while(node) {
            newNode->random = old2NewHash[node->random];
            node = node->next;
            newNode = newNode->next;
        }
        return newHead;
    }
};
```