2579. Count Total Number of Colored Cells

There exists an infinitely large two-dimensional grid of uncolored unit cells. You are given a positive integer `n`, indicating that you must do the following routine for `n` minutes:

* At the first minute, color any arbitrary unit cell blue.
* Every minute thereafter, color blue every uncolored cell that touches a blue cell.

Below is a pictorial representation of the state of the grid after minutes `1`, `2`, and `3`.

![2579_example-copy-2.png](img/2579_example-copy-2.png)

Return the number of **colored cells** at the end of `n` minutes.

 

**Example 1:**
```
Input: n = 1
Output: 1
Explanation: After 1 minute, there is only 1 blue cell, so we return 1.
```

**Example 2:**
```
Input: n = 2
Output: 5
Explanation: After 2 minutes, there are 4 colored cells on the boundary and 1 in the center, so we return 5. 
```

**Constraints:**

* `1 <= n <= 10^5`

# Submissions
---
**Solution 1: (DP)**
```
Runtime: 5 ms
Memory: 6 MB
```
```c++
class Solution {
public:
    long long coloredCells(int n) {
        long long ans=1;
        if (n==1) {
            return ans;
        }
        for (long long i = 1; i < n; i++) {
            ans += (4*i);
        }
        return ans;
    }
};
```

**Solution 2: (Math)**
```
Runtime: 0 ms
Memory: 6 MB
```
```c++
class Solution {
public:
    long long coloredCells(int n) {
        long long t = n;
        return t*t + (t-1)*(t-1);
    }
};
```

**Solution 3: (DP Bottom-Up)**

      *            1

      *
    * * *          1+4
      *             (4*1)
      v
    v * v 
  v * * * v        5+8
    v * v           (4*2)
      v

      v
    v * v
  V * * * v
v * * * * * v      13+12 
  v * * * v          (4*3)
    v * v
      v

```
Runtime: 0 ms, Beats 100.00%
Memory: 7.92 MB, Beats 31.17%
```
```c++
class Solution {
public:
    long long coloredCells(int n) {
        if (n == 1) {
            return 1;
        }
        int i = 2;
        long long pre = 1, cur;
        while (i <= n) {
            cur = pre + (i-1)*4;
            pre = cur;
            i += 1;
        }
        return pre;
    }
};
```

**Solution 4: (Math)**

1 + 4*1 + 4*2 + ... + 4*(n-1)
= 1 + 4*n*(n-1)/2
= 1 + 2*n*(n-1)

```
Runtime: 0 ms, Beats 100.00%
Memory: 7.86 MB, Beats 61.42%
```
```c++
class Solution {
public:
    long long coloredCells(int n) {
        return 1 + (long long)n * (n - 1) * 2; 
    }
};
```
