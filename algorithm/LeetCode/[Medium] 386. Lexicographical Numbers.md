386. Lexicographical Numbers

Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.

# Submissions
---
**Solution 1: (String)**
```
Runtime: 116 ms
Memory Usage: 21.2 MB
```
```python
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return map(int, sorted([str(i) for i in range(1, n+1)]))
```

**Solution 2: (DFS, Time: O(n), Space: O(long_10 (n)))**

n = 130

    1 
    1 0
    1 0 0
        9
      1
      1 0
        9
      2
      2 0
        9
      3
      3 0
    1 4
    1 9
    2
    9

```
Runtime: 7 ms, Beats 27.30%
Memory: 13.96 MB, Beats 83.88%
```
```c++
class Solution {
    void dfs(int cur, int n, vector<int> &ans) {
        if (cur > n) {
            return;
        }
        ans.push_back(cur);
        for (int j = 0; j < 10; j ++) {
            dfs(cur*10 + j, n, ans);
        }
    }
public:
    vector<int> lexicalOrder(int n) {
        vector<int> ans;
        for (int i = 1; i < 10; i ++) {
            dfs(i, n, ans);
        }
        return ans;
    }
};
```

**Solution 2: (Iterative, Time: O(n), Space: O(1))**

192
    1
    1 0
    1 0 0
    1 0 9
    1 1 0
    1 1 9
    1 9 0
    1 9 2
    2
    2 0
    2 9
    9
    9 0
    9 9

```
Runtime: 0 ms, Beats 100.00%
Memory: 14.06 MB, Beats 69.54%
```
```c++
class Solution {
public:
    vector<int> lexicalOrder(int n) {
        int cur = 1, k = 0;
        vector<int> ans;
        while (k < n) {
            ans.push_back(cur);
            k += 1;
            if (cur*10 <= n) {
                cur = cur*10;
            } else {
                while (cur%10 == 9 || cur == n) {
                    cur /= 10;
                }
                cur += 1;
            }
        }
        return ans;
    }
};
```
