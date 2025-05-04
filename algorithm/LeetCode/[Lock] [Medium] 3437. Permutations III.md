3437. Permutations III

Given an integer `n`, an **alternating permutation** is a permutation of the first `n` positive integers such that no **two** adjacent elements are **both** odd or **both** even.

Return all such **alternating permutations** sorted in lexicographical order.

 

**Example 1:**
```
Input: n = 4

Output: [[1,2,3,4],[1,4,3,2],[2,1,4,3],[2,3,4,1],[3,2,1,4],[3,4,1,2],[4,1,2,3],[4,3,2,1]]
```

**Example 2:**
```
Input: n = 2

Output: [[1,2],[2,1]]

Example 3:

Input: n = 3

Output: [[1,2,3],[3,2,1]]
```
 

**Constraints:**

* `1 <= n <= 10`

# Submissions
---
**Solution 1: (Backtracking)**
```
Runtime: 9 ms, Beats 94.51%
Memory: 18.34 MB, Beats 67.03%
```
```c++
class Solution {
    void bt(int a, int n, vector<int> &visited, vector<int> &cur, vector<vector<int>> &ans) {
        if (cur.size() == n) {
            ans.push_back(cur);
            return;
        }
        for (int b = 1; b <= n; b ++) {
            if (b != a && !visited[b] && a%2 != b%2) {
                visited[b] = 1;
                cur.push_back(b);
                bt(b, n, visited, cur, ans);
                visited[b] = 0;
                cur.pop_back();
            }
        }
    }
public:
    vector<vector<int>> permute(int n) {
        vector<int> visited(n+1), cur;
        vector<vector<int>> ans;
        for (int a = 1; a <= n; a ++) {
            visited[a] = 1;
            cur.push_back(a);
            bt(a, n, visited, cur, ans);
            visited[a] = 0;
            cur.pop_back();
        }
        return ans;
    }
};
```
