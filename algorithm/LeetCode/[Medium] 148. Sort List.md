148. Sort List

Sort a linked list in O(n log n) time using constant space complexity.

**Example 1:**
```
Input: 4->2->1->3
Output: 1->2->3->4
```

**Example 2:**
```
Input: -1->5->3->4->0
Output: -1->0->3->4->5
```

# Submissions
---
**Solution: (Top Down Merge Sort)**

* Time: O(nlogn)
* Space: O(logn)

```
Runtime: 131 ms
Memory Usage: 29.1 MB
```
```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* sortList(ListNode* head) {
        if (!head || !head->next)
            return head;
        ListNode* mid = getMid(head);
        ListNode* left = sortList(head);
        ListNode* right = sortList(mid);
        return merge(left, right);
    }

    ListNode* merge(ListNode* list1, ListNode* list2) {
        ListNode dummyHead(0);
        ListNode* ptr = &dummyHead;
        while (list1 && list2) {
            if (list1->val < list2->val) {
                ptr->next = list1;
                list1 = list1->next;
            } else {
                ptr->next = list2;
                list2 = list2->next;
            }
            ptr = ptr->next;
        }
        if(list1) ptr->next = list1;
        else ptr->next = list2;

        return dummyHead.next;
    }

    ListNode* getMid(ListNode* head) {
        ListNode* midPrev = nullptr;
        while (head && head->next) {
            midPrev = (midPrev == nullptr) ? head : midPrev->next;
            head = head->next->next;
        }
        ListNode* mid = midPrev->next;
        midPrev->next = nullptr;
        return mid;
    }
};
```

**Solution: (Bottom Up Merge Sort)**

* Time: O(nlogn)
* Space: O(1)

```
Runtime: 104 ms
Memory Usage: 29 MB
```
```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* tail = new ListNode();
    ListNode* nextSubList = new ListNode();
    
    ListNode* sortList(ListNode* head) {
        if (!head || !head -> next)
            return head;
        int n = getCount(head);
        ListNode* start = head;
        ListNode dummyHead(0);
        for (int size = 1; size < n; size = size * 2) {
            tail = &dummyHead;
            while (start) {
                if (!start->next) {
                    tail->next = start;
                    break;
                }
                ListNode* mid = split(start, size);
                merge(start, mid);
                start = nextSubList;
            }
            start = dummyHead.next;
        }
        return dummyHead.next;
    }

    ListNode* split(ListNode* start, int size) {
        ListNode* midPrev = start;
        ListNode* end = start->next;
        //use fast and slow approach to find middle and end of second linked list
        for (int index = 1; index < size && (midPrev->next || end->next); index++) {
            if (end->next) {
                end = (end->next->next) ? end->next->next : end->next;
            }
            if (midPrev->next) {
                midPrev = midPrev->next;
            }
        }
        ListNode* mid = midPrev->next;
        nextSubList = end->next;
        midPrev->next = nullptr;
        end->next = nullptr;
        // return the start of second linked list
        return mid;
    }

    void merge(ListNode* list1, ListNode* list2) {
        ListNode dummyHead(0);
        ListNode* newTail = &dummyHead;
        while (list1 && list2) {
            if (list1->val < list2->val) {
                newTail->next = list1;
                list1 = list1->next;
                newTail = newTail->next;
            } else {
                newTail->next = list2;
                list2 = list2->next;
                newTail = newTail->next;
            }
        }
        newTail->next = (list1) ? list1 : list2;
        // traverse till the end of merged list to get the newTail
        while (newTail->next) {
            newTail = newTail->next;
        }
        // link the old tail with the head of merged list
        tail->next = dummyHead.next;
        // update the old tail with the new tail of merged list
        tail = newTail;
    }

    int getCount(ListNode* head) {
        int cnt = 0;
        ListNode* ptr = head;
        while (ptr) {
            ptr = ptr->next;
            cnt++;
        }
        return cnt;
    }
};
```

**Solution 1: (Sort, Linked list, Merge Sort, Top-Down)**
```
Runtime: 236 ms
Memory Usage: 21.9 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(h1, h2):
            cur = dummy = ListNode(-1)
            while h1 and h2:
                if h1.val < h2.val:
                    cur.next, h1 = h1, h1.next
                else:
                    cur.next, h2 = h2, h2.next
                cur = cur.next
            cur.next = h1 or h2
            return dummy.next
        
        if not head or not head.next: return head
        pres = slow = fast = head
        while fast and fast.next:
            pres = slow
            slow = slow.next
            fast = fast.next.next
        pres.next = None  #cut off in the middle
        first = self.sortList(head)
        second = self.sortList(slow)
        return merge(first, second)
```

**Solution 2: (Linked List, Merge Sort)**
```
Runtime: 40 ms
Memory Usage: 14.2 MB
```
```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *mergeList(struct ListNode *l1, struct ListNode *l2)
{
    if(l1 == NULL) return l2;
    if(l2 == NULL) return l1;

    if(l1->val <= l2->val)
    {
        l1->next = mergeList(l1->next, l2);
        return l1;
    }
    else
    {
        l2->next = mergeList(l1, l2->next);
        return l2;
    }
}

struct ListNode* sortList(struct ListNode* head){
    if(head == NULL)
        return NULL;
    if(head->next == NULL)
        return head;
    struct ListNode *fast, *slow, *pre;
    fast = slow = head;
    while(fast && fast->next)
    {
        pre = slow;
        fast = fast->next->next;
        slow = slow->next;
    }

    pre->next = NULL;
    return mergeList(sortList(head), sortList(slow));
}
```
