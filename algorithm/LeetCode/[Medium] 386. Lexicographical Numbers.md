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
    2
    2 0
      9
    3
    3 0

```
Runtime: 12 ms
```
```c++
class Solution {
    void dfs(int v, vector<int> &ans, int n) {
        if (v > n) {
            return;
        }
        ans.push_back(v);
        for (int i = 0; i <= 9; i ++) {
            dfs(v*10 + i, ans, n);
        }
    }
public:
    vector<int> lexicalOrder(int n) {
        vector<int> ans;
        for (int v = 1; v <= 9; v ++) {
            dfs(v, ans, n);
        }
        return ans;
    }
};
```

**Solution 2: (Iterative, Time: O(n), Space: O(1))**
```
Runtime: 3 ms
Memory: 12.45 MB
```
```c++
class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector<int> ans;
        int cur = 1;

        // Generate numbers from 1 to n
        for (int i = 0; i < n; ++i) {
            ans.push_back(cur);

            // If multiplying the current number by 10 is within the limit, do
            // it
            if (cur * 10 <= n) {
                cur *= 10;
            } else {
                // Adjust the current number by moving up one digit
                while (cur % 10 == 9 || cur >= n) {
//                    ^^^^^^^^^^^^^^
//              ex. 18 -> 19 -> 2 -> 20
//                        ^^^^^^^
                    cur /= 10;  // Remove the last digit
                }
                cur += 1;  // Increment the number
            }
        }

        return ans;
    }
};
```
