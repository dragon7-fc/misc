2929. Distribute Candies Among Children II

You are given two positive integers `n` and `limit`.

Return the total number of ways to distribute `n` candies among `3` children such that no child gets more than `limit` candies.

 

**Example 1:**
```
Input: n = 5, limit = 2
Output: 3
Explanation: There are 3 ways to distribute 5 candies such that no child gets more than 2 candies: (1, 2, 2), (2, 1, 2) and (2, 2, 1).
```

**Example 2:**
```
Input: n = 3, limit = 3
Output: 10
Explanation: There are 10 ways to distribute 3 candies such that no child gets more than 3 candies: (0, 0, 3), (0, 1, 2), (0, 2, 1), (0, 3, 0), (1, 0, 2), (1, 1, 1), (1, 2, 0), (2, 0, 1), (2, 1, 0) and (3, 0, 0).
```

**Constraints:**

* `1 <= n <= 10^6`
* `1 <= limit <= 10^6`

# Submissions
---
**Solution 1: (Math, two pointer)**
```
Runtime: 27 ms
Memory: 6.3 MB
```
```c++
class Solution {
public:
    long long distributeCandies(int n, int limit) {
        long long ans = 0;
        int firstMin = max(0, n - 2*limit);
        int firstMax = min(limit, n);
        for(int i = firstMin; i <= firstMax; ++i ){
            int secondMin = max(0, n - i - limit);
            int secondMax = min(limit, n - i);
            ans += secondMax - secondMin + 1;
        }
        return ans;
    }
};
```

**Solution 2: (Enumeration)**

    n = 5, limit = 2
    0  1  2  3  4  5
    ^x
       ^x
          ^x
       1  2
ans    1  3

    x = 2 -> y + z = 3
    0  1  2  3
          ^min(n-x-0, limit)
                   ^  ^^^^^
                   y    z
       ^max(0, n-x-limit)
            ^      ^^^^^
            z        y
             
    n = 3, limit = 3
    0  1  2  3
    ----------
    ^x
       -------
       ^x
          ----
          ^x
             -
             ^x
ans 4  7  9  10

```
Runtime: 36 ms, Beats 12.35%
Memory: 8.98 MB, Beats 57.06%
```
```c++
class Solution {
public:
    long long distributeCandies(int n, int limit) {
        long long ans = 0;
        for (int i = 0; i <= min(limit, n); i++) {
            if (n - i > 2 * limit) {
                continue;
            }
            ans += min(n - i, limit) - max(0, n - i - limit) + 1;
        }
        return ans;
    }
};
```

**Solution 3: (Inclusion-Exclusion Principle)**
```
Runtime: 5 ms, Beats 77.06%
Memory: 9.03 MB, Beats 18.82%
```
```c++
class Solution {
    long long cal(int x) {
        if (x < 0) {
            return 0;
        }
        return (long)x * (x - 1) / 2;
    }
public:
    long long distributeCandies(int n, int limit) {
        return cal(n + 2) - 3 * cal(n - limit + 1) +
//             ^^^^^^^^^^
//             Total number of unrestricted distributions:
//                          ^^^^^^^^^^^^^^^^^^^^^^
//                          At least one child receives more than limit candies:
               3 * cal(n - (limit + 1) * 2 + 2) - cal(n - 3 * (limit + 1) + 2);
//             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
//             At least two children receive more than limit candies:
//                                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
//                                                All three children receive more than limit candies:
    }
};
```
