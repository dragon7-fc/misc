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
**Solution 1: (Hash Table, Linked List, address as key)**
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

**Solution 3: (Linked List)**
```
Runtime: 15 ms
Memory Usage: 8.4 MB
```
```c
/**
 * Definition for a Node.
 * struct Node {
 *     int val;
 *     struct Node *next;
 *     struct Node *random;
 * };
 */

struct Node *newNode(){
    struct Node *new = (struct Node *)malloc(sizeof(struct Node));
    new->next=NULL;
    new->random=NULL;
    
    return new;
}

struct Node* copyRandomList(struct Node* head) {
    if(!head) return NULL;
    
    struct Node *aux;
    struct Node *curr = head;
    struct Node *copy;
    
    //copy each node
    while(curr){
        aux = newNode();
        aux->val = curr->val;
        aux->next = curr->next;
        curr->next = aux;
        curr = aux->next;
    }

    curr = head;
    copy = head->next;
    
    //set random pointer
    while(curr){
        curr->next->random = (curr->random == NULL ? NULL : curr->random->next);
        curr = curr->next->next;
    }
    
    curr = head;
    
    //fix next pointer
    while(curr->next){
        aux = curr->next;
        curr->next = curr->next->next;
        curr = aux;
    }
    
    return copy;
}
```

**Solution 4: (Hash Table, Linked List, address as key)**
```
Runtime: 8 ms
Memory Usage: 11.5 MB
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
    unordered_map<Node*, Node*> m;
public:
    Node* copyRandomList(Node* head) {
        if (!head){
            return nullptr;
        }
        if (m.count(head)) {
            return m[head];
        }
        Node *node = new Node(head->val);
        m[head] = node;
        node->next = copyRandomList(head->next);
        node->random = copyRandomList(head->random);
        return node;
    }
};
```
