1019. Next Greater Node In Linked List

We are given a linked list with `head` as the first node.  Let's number the nodes in the list: `node_1, node_2, node_3, ...` etc.

Each node may have a next larger **value**: for `node_i`, `next_larger(node_i)` is the `node_j.val` such that `j > i`, `node_j.val > node_i.val`, and `j` is the smallest possible choice.  If such a `j` does not exist, the next larger value is `0`.

Return an array of integers answer, where `answer[i] = next_larger(node_{i+1})`.

Note that in the example **inputs** (not outputs) below, arrays such as `[2,1,5]` represent the serialization of a linked list with a head node value of `2`, second node value of `1`, and third node value of `5`.

**Example 1:**
```
Input: [2,1,5]
Output: [5,5,0]
```

**Example 2:**
```
Input: [2,7,4,3,5]
Output: [7,0,5,5,0]
```

**Example 3:**
```
Input: [1,7,5,1,9,2,5,1]
Output: [7,9,9,9,0,5,0,0]
```

Note:

1. 1 <= node.val <= 10^9 for each node in the linked list.
1. The given list has length in the range [0, 10000].

# Sobmissions
---
**Solution 1: (Stack, Linked List)**
```
Runtime: 368 ms
Memory Usage: 18.2 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack = []
        cur = head
        while cur:
            while stack and cur.val > stack[-1].val:
                node = stack.pop()
                node.val = cur.val
            stack.append(cur)
            cur = cur.next
        
        for node in stack:
            node.val = 0
        
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        
        return res
```
**Solution 2: (Stack, Linked List)**
```
Runtime: 193 ms
Memory Usage: 34.2 MB
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
int* nextLargerNodes(struct ListNode* head, int* returnSize){
    int top = -1, i = 0, *ans;
    struct ListNode **stack, *cur = head;
    stack = malloc(10000*sizeof(struct ListNode *));
    while (cur) {
        while (top >= 0 && cur->val > stack[top]->val)
            stack[top--]->val = cur->val;
        stack[++top] = cur;
        cur = cur->next;
        i += 1;
    }
    *returnSize = i;
    ans = malloc(i*sizeof(int));
    if (top >= 0) {
        for (int i = 0; i <= top; i ++){
            stack[i]->val = 0;
        }
    }
    cur = head;
    i = 0;
    while (cur) {
        ans[i] = cur->val;
        cur = cur->next;
        i += 1;
    }
    return ans;
}
```

**Solution 3: (Stack, mono dec stack)**
```
Runtime: 65 ms
Memory: 45.03 MB
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
    vector<int> nextLargerNodes(ListNode* head) {
        stack<pair<int,int>> stk;
        vector<int> ans;
        int i  = 0;
        while (head) {
            while (stk.size() && stk.top().second < head->val) {
                ans[stk.top().first] = head->val;
                stk.pop();
            }
            stk.push({i, head->val});
            ans.push_back(0);
            i += 1;
            head = head->next;
        }
        return ans;
    }
};
```

**Solution 3: (Stack, mono dec stack, walk backward)**
```
Runtime: 2 ms, Beats 87.58%
Memory: 42.10 MB, Beats 99.43%
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
    vector<int> nextLargerNodes(ListNode* head) {
        int n = 0;
        ListNode *pre = nullptr, *cur = head, *ncur;
        stack<int> stk;
        while (cur) {
            n += 1;
            ncur = cur->next;
            cur->next = pre;
            pre = cur;
            cur = ncur;
        }
        vector<int> ans(n);
        while (pre) {
            n -= 1;
            while (stk.size() && stk.top() <= pre->val) {
                stk.pop();
            }
            if (stk.size()) {
                ans[n] = stk.top();
            }
            stk.push(pre->val);
            pre = pre->next;
        }
        return ans;
    }
};
```
