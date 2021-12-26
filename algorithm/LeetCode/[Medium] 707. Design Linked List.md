707. Design Linked List

Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are `0`-indexed.

Implement these functions in your linked list class:

* `get(index)` : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
* `addAtHead(val)` : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
* `addAtTail(val)` : Append a node of value val to the last element of the linked list.
* `addAtIndex(index, val)` : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the * * length, the node will not be inserted. If index is negative, the node will be inserted at the head of the list.
* `deleteAtIndex(index)` : Delete the index-th node in the linked list, if the index is valid.

**Example:**
```
MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3
```

Note:

* All values will be in the range of [1, 1000].
* The number of operations will be in the range of [1, 1000].
* Please do not use the built-in LinkedList library

# Submissions
---
**Solution 1: (Linked list)**
```
Runtime: 312 ms
Memory Usage: 14.1 MB
```
```python
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dummy = Node(0)
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self.dummy.next
        while node:
            if index == 0:
                return node.val
            index -= 1
            node = node.next
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        node.next = self.dummy.next
        self.dummy.next = node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        prev, cur = self.dummy, self.dummy.next
        while  cur:
            prev = cur
            cur = cur.next
        prev.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. If index is negative, the node will be inserted at the head of the list.
        """
        if index < 0:
            self.addAtHead(val)
        else: 
            prev, cur = self.dummy, self.dummy.next
            while cur:
                if index == 0:
                    node = Node(val)
                    node.next = prev.next
                    prev.next = node
                    return

                index -= 1
                prev = cur
                cur = cur.next

            if index == 0:
                prev.next = Node(val)
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        prev, cur = self.dummy, self.dummy.next
        while cur:
            if index == 0:
                prev.next = cur.next
                return
            
            index -= 1
            prev = cur
            cur = cur.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
```

**Solution 2: (Linked List)**
```
Runtime: 44 ms
Memory Usage: 13.7 MB
```
```c

typedef struct {
    int n;
    struct ListNode *node;
} MyLinkedList;


MyLinkedList* myLinkedListCreate() {
    MyLinkedList *rst = calloc(1, sizeof(MyLinkedList));
    return rst;
}

int myLinkedListGet(MyLinkedList* obj, int index) {
    struct ListNode *node = obj->node;
    if (index >= obj->n)
        return -1;
    while (index) {
        index -= 1;
        node = node->next;
    }
    return node->val;
}

void myLinkedListAddAtHead(MyLinkedList* obj, int val) {
    struct ListNode *node = calloc(1, sizeof(struct ListNode));
    node->val = val;
    if (!obj->node) {
        obj->node = node;
    } else {
        node->next = obj->node;
        obj->node = node;
    }
    obj->n += 1;
}

void myLinkedListAddAtTail(MyLinkedList* obj, int val) {
    struct ListNode *prev = NULL, *cur = obj->node, *node = calloc(1, sizeof(struct ListNode));
    node->val = val;
    while (cur) {
        prev = cur;
        cur = cur->next;
    }
    if (prev)
        prev->next = node;
    else
        obj->node = node;
    obj->n += 1;
}

void myLinkedListAddAtIndex(MyLinkedList* obj, int index, int val) {
    if (index > obj->n) {
        return;
    }
    struct ListNode *prev = NULL, *cur = obj->node, *node = calloc(1, sizeof(struct ListNode));
    node->val = val;
    while (index) {
        prev = cur;
        cur = cur->next;
        index -= 1;
    }
    node->next = cur;
    if (prev)
        prev->next = node;
    else
        obj->node = node;
    obj->n += 1;
}

void myLinkedListDeleteAtIndex(MyLinkedList* obj, int index) {
    struct ListNode *prev = NULL, *cur = obj->node;
    if (index >= obj->n)
        return;
    while (index) {
        prev = cur;
        cur = cur->next;
        index -= 1;
    }
    if (prev)
        prev->next = cur->next;
    else
        obj->node = cur->next;
    free(cur);
    obj->n -= 1;
}

void myLinkedListFree(MyLinkedList* obj) {
    struct ListNode *cur = obj->node, *next;
    while (cur) {
        next = cur->next;
        free(cur);
        cur = next;
    }
    free(obj);
}

/**
 * Your MyLinkedList struct will be instantiated and called as such:
 * MyLinkedList* obj = myLinkedListCreate();
 * int param_1 = myLinkedListGet(obj, index);
 
 * myLinkedListAddAtHead(obj, val);
 
 * myLinkedListAddAtTail(obj, val);
 
 * myLinkedListAddAtIndex(obj, index, val);
 
 * myLinkedListDeleteAtIndex(obj, index);
 
 * myLinkedListFree(obj);
*/
```
