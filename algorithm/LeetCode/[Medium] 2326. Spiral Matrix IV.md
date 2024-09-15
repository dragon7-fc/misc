2326. Spiral Matrix IV

You are given two integers `m` and `n`, which represent the dimensions of a matrix.

You are also given the head of a linked list of integers.

Generate an `m x n` matrix that contains the integers in the linked list presented in **spiral** order (**clockwise**), starting from the **top-left** of the matrix. If there are remaining empty spaces, fill them with `-1`.

Return the generated matrix.

 

**Example 1:**

```
Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
Explanation: The diagram above shows how the values are printed in the matrix.
Note that the remaining spaces in the matrix are filled with -1.
```

**Example 2:**

```
Input: m = 1, n = 4, head = [0,1,2]
Output: [[0,1,2,-1]]
Explanation: The diagram above shows how the values are printed from left to right in the matrix.
The last space in the matrix is set to -1.
```

**Constraints:**

 * `1 <= m, n <= 10^5`
 * `1 <= m * n <= 10^5`
 * The number of nodes in the list is in the range `[1, m * n]`.
 * `0 <= Node.val <= 1000`

# Submissions
---
**Solution 1: (Linked-List)**
```
Runtime: 2687 ms
Memory Usage: 66.1 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        num = m * n
        res = [[-1 for j in range(n)] for i in range(m)]
        x, y = 0, 0
        dx, dy = 1, 0
        while head:
            res[y][x] = head.val
            if x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= m or res[y+dy][x+dx] != -1:
                dx, dy = -dy, dx
            x = x + dx
            y = y + dy
            head = head.next
        return res
```

**Solution 2: (Linked-List)**
```
Runtime: 154 ms
Memory: 130.61 MB
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
    int d[5] = {0, 1, 0, -1, 0};
public:
    vector<vector<int>> spiralMatrix(int m, int n, ListNode* head) {
        vector<vector<int>> ans(m, vector<int>(n, -1));
        int r = 0, c = 0, nr, nc, nd = 0;
        while (head) {
            ans[r][c] = head->val;
            head = head->next;
            nr = r + d[nd];
            nc = c + d[nd+1];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n || ans[nr][nc] != -1) {
                nd = (nd+1)%4;
            }
            r = r + d[nd];
            c = c + d[nd+1];
        }
        return ans;
    }
};
```
