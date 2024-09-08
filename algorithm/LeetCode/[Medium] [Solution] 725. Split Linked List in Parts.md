725. Split Linked List in Parts

Given a (singly) linked list with head node `root`, write a function to split the linked list into `k` consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should have a size differing by more than `1`. This may lead to some parts being `null`.

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

# Solution
---
## Approach #1: Create New Lists [Accepted]

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

Our solution proceeds similarly. For a part of size `L = width + (i < remainder ? 1 : 0)`, instead of stepping `L` times, we will step `L-1` times, and our final time will also sever the link between the last node from the previous part and the first node from the next part.

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

# Submissions
---
**Solution 1: (Split Input List, Linked List)**
```
Runtime: 44 ms
Memory Usage: 13.8 MB
```
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

**Solution 2: (Linked List)**
```
Runtime: 8 ms
Memory Usage: 8.8 MB
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
    int countNodes(ListNode* head) {
        int n = 0;
        while (head) {
            n++;
            head = head->next;
        }
        return n;
    }
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        int n = countNodes(head);
        int part_size = n / k, left = n % k;
        ListNode *ptr = head, *prev = NULL;
        
        vector<ListNode*> res(k);
        for (int i = 0; i < k; i++) {
            res[i] = head;
            
            for (int j = 0; j < part_size + (i < left); j++) {
                prev = head; 
                head = head->next; 
            }
            if (prev) prev->next = NULL;
        }
        
        return res;
    }
};
```

**Solution 3: (Linked List)**
```
Runtime: 4 ms
Memory Usage: 6.6 MB
```
```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
struct ListNode** splitListToParts(struct ListNode* head, int k, int* returnSize){
    struct ListNode *prev, *cur;
    struct ListNode **ans = malloc(sizeof(struct ListNode *)*k);
    int N = 0, DIV, MOD;
    cur = head;
    while (cur) {
        N += 1;
        cur = cur->next;
    }
    prev = NULL;
    cur = head;
    DIV = N/k, MOD = N%k;
    for (int i = 0; i < k; i ++) {
        ans[i] = cur;
        for (int j = 0; j < DIV && cur; j ++) {
            prev = cur;
            cur = cur->next;
        }
        if (i < MOD && cur) {
            prev = cur;
            cur = cur->next;
        }
        if (prev)
            prev->next = NULL;
    }
    *returnSize = k;
    return ans;
}
```

**Solution 4: (Linked List)**
```
Runtime: 4 ms
Memory Usage: 6.8 MB
```
```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
struct ListNode** splitListToParts(struct ListNode* head, int k, int* returnSize){
    int counter=0;
    struct ListNode* ptr;
    struct ListNode** ret_array; 
    int count_array[k];
    int i, j;
    ptr = head;
    while (ptr!=NULL) { counter++; ptr = ptr->next; }
    ret_array = calloc(1, k * sizeof(struct ListNode*));
    *returnSize = k;
    for (i=0; i<k; i++) count_array[i]=counter/k;
    for (i=0; i<(counter % k); i++) count_array[i]++;
    for (i=0; i<k; i++) {
        ret_array[i]=head;
        ptr=head;
        for (j=1; j<count_array[i]; j++) ptr = ptr->next;
        if (ptr!=NULL) {
            head=ptr->next;
            ptr->next=NULL;
        }
    }
    return ret_array;
}
```

**Solution 5: (Linked List)**
```
Runtime: 6 ms
Memory: 8.9 MB
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
    void dfs(ListNode *cur, int i, int d, int r, int k, vector<ListNode *> &ans) {
        if (!cur) {
            return;
        }
        ListNode *pre;
        ans[i] = cur;
        for (int j = 0; cur && j < d + (r > 0); j ++) {
            pre = cur;
            cur = cur->next;
        }
        pre->next = nullptr;
        dfs(cur, i+1, d, r-1, k, ans);
    }
public:
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        int n = 0;
        ListNode *cur = head;
        vector<ListNode *> ans(k, nullptr);
        while (cur) {
            n += 1;
            cur = cur->next;
        }
        dfs(head, 0, n/k, n%k, k, ans);
        return ans;
    }
};
```

**Solution 6: (Linked List)**
```
Runtime: 0 ms
Memory: 8.9 MB
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
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        // Create a vector of ListNode pointers to store the k parts.
        vector<ListNode*> parts(k, nullptr);

        // Calculate the length of the linked list.
        int len = 0;
        for (ListNode* node = head; node; node = node->next)
            len++;

        // Calculate the minimum guaranteed part size (n) and the number of extra nodes (r).
        int n = len / k, r = len % k;

        // Initialize pointers to traverse the linked list.
        ListNode* node = head, *prev = nullptr;

        // Loop through each part.
        for (int i = 0; node && i < k; i++, r--) {
            // Store the current node as the start of the current part.
            parts[i] = node;
            // Traverse n + 1 nodes if there are remaining extra nodes (r > 0).
            // Otherwise, traverse only n nodes.
            for (int j = 0; j < n + (r > 0); j++) {
                prev = node;
                node = node->next;
            }
            // Disconnect the current part from the rest of the list by setting prev->next to nullptr.
            prev->next = nullptr;
        }

        // Return the array of k parts.
        return parts;
    }
};
```

**Solution 7: (Linked List)**
```
Runtime: 4 ms
Memory: 13.88 MB
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
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        int sz = 0, d, r;
        ListNode *cur = head, *pre;
        while (cur) {
            sz += 1;
            cur = cur->next;
        }
        d = sz/k;
        r = sz%k;
        vector<ListNode*> ans;
        for (int i = 0; i < k; i ++) {
            cur = head;
            ans.push_back(cur);
            pre = nullptr;
            for (int j = 0; j < d + (r > 0); j ++) {
                if (head) {
                    head = head->next;
                }
                pre = cur;
                if (cur) {
                    cur = cur->next;
                }
            }
            if (pre) {
                pre->next = nullptr;
            }
            r -= 1;
        }
        return ans;
    }
};
```
