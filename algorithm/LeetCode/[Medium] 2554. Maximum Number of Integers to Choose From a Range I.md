2554. Maximum Number of Integers to Choose From a Range I

You are given an integer array `banned` and two integers `n` and `maxSum`. You are choosing some number of integers following the below rules:

* The chosen integers have to be in the range `[1, n]`.
* Each integer can be chosen **at most once**.
* The chosen integers should not be in the array `banned`.
* The sum of the chosen integers should not exceed `maxSum`.

Return the **maximum** number of integers you can choose following the mentioned rules.

 

**Example 1:**
```
Input: banned = [1,6,5], n = 5, maxSum = 6
Output: 2
Explanation: You can choose the integers 2 and 4.
2 and 4 are from the range [1, 5], both did not appear in banned, and their sum is 6, which did not exceed maxSum.
```

**Example 2:**
```
Input: banned = [1,2,3,4,5,6,7], n = 8, maxSum = 1
Output: 0
Explanation: You cannot choose any integer while following the mentioned conditions.
```

**Example 3:**
```
Input: banned = [11], n = 7, maxSum = 50
Output: 7
Explanation: You can choose the integers 1, 2, 3, 4, 5, 6, and 7.
They are from the range [1, 7], all did not appear in banned, and their sum is 28, which did not exceed maxSum.
```

**Constraints:**

* `1 <= banned.length <= 10^4`
* `1 <= banned[i], n <= 10^4`
* `1 <= maxSum <= 10^9`

# Submissions
---
**Solution 1: (Set)**
```
Runtime: 1248 ms
Memory: 16 MB
```
```python
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        s = set(banned)
        cur = 1
        acc = ans = 0
        while cur <= n:
            if cur not in s and cur+acc <= maxSum:
                acc += cur
                ans += 1
            cur += 1
        return ans
```

**Solution 2: (Sort)**
```
Runtime: 42 ms
Memory: 117.64 MB
```
```c++
class Solution {
public:
    int maxCount(vector<int>& banned, int n, int maxSum) {
        int m = banned.size(), i = 0, a = 1, cur = 0, ans = 0;
        sort(banned.begin(), banned.end());
        while (i < m && a <= n && cur + a <= maxSum) {
            if (a != banned[i]) {
                cur += a;
                ans += 1;
            } else {
                while (i+1 < m && banned[i] == a) {
                    i += 1;
                }
            }
            a += 1;
        }
        return ans;
    }
};
```

**Solution 2: (Set)**
```
Runtime: 198 ms
Memory: 177.76 MB
```
```c++
class Solution {
public:
    int maxCount(vector<int>& banned, int n, int maxSum) {
        int a = 1, cur = 0, ans = 0;
        unordered_set<int> st(banned.begin(), banned.end());
        while (a <= n && cur + a <= maxSum) {
            if (!st.count(a)) {
                cur += a;
                ans += 1;
            }
            a += 1;
        }
        return ans;
    }
};
```
