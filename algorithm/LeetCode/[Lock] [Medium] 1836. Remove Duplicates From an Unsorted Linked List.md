1836. Remove Duplicates From an Unsorted Linked List

Given the `head` of a linked list, find all the values that appear **more than once** in the list and delete the nodes that have any of those values.

Return the linked list after the deletions.

 

**Example 1:**

![1836_tmp-linked-list.jpg](img/1836_tmp-linked-list.jpg)
```
Input: head = [1,2,3,2]
Output: [1,3]
Explanation: 2 appears twice in the linked list, so all 2's should be deleted. After deleting all 2's, we are left with [1,3].
```

**Example 2:**

![1836_tmp-linked-list-1.jpg](img/1836_tmp-linked-list-1.jpg)
```
Input: head = [2,1,1,2]
Output: []
Explanation: 2 and 1 both appear twice. All the elements should be deleted.
```

**Example 3:**

![](1836_tmp-linked-list-2.jpg)(img/1836_tmp-linked-list-2.jpg)
```
Input: head = [3,2,2,1,3,2,4]
Output: [1,4]
Explanation: 3 appears twice and 2 appears three times. After deleting all 3's and 2's, we are left with [1,4].
```

**Constraints:**

* The number of nodes in the list is in the range `[1, 10^5]`
* `1 <= Node.val <= 10^5`

# Submissions
---
**Solution 1: (Linked List)**
```
Runtime: 172 ms
Memory Usage: 50.4 MB
```
```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* deleteDuplicatesUnsorted(struct ListNode* head){
    int data[100000] = {0};
    struct ListNode *curNode = head, *dummy, *tmpNode;
    while (curNode) {
        data[curNode->val-1] += 1;
        curNode = curNode->next;
    }
    dummy = calloc(1, sizeof(struct ListNode));
    dummy->next = head;
    tmpNode = dummy;
    curNode = head;
    while (curNode) {
        if (data[curNode->val-1] == 1) {
            tmpNode->next = curNode;
            tmpNode = tmpNode->next;
        } else {
            tmpNode->next = NULL;
        }
        curNode = curNode->next;
    }

    return dummy->next; 
}
```
