3857. Minimum Cost to Split into Ones

You are given an integer `n`.

In one operation, you may split an integer `x` into two positive integers `a` and `b` such that `a + b = x`.

The cost of this operation is `a * b`.

Return an integer denoting the **minimum** total cost required to split the integer n into `n` ones.

 

**Example 1:**
```
Input: n = 3

Output: 3

Explanation:

One optimal set of operations is:

x	a	b	a + b	a * b	Cost
3	1	2	3	2	2
2	1	1	2	1	1
Thus, the minimum total cost is 2 + 1 = 3.
```

**Example 2:**
```
Input: n = 4

Output: 6

Explanation:

One optimal set of operations is:

x	a	b	a + b	a * b	Cost
4	2	2	4	4	4
2	1	1	2	1	1
2	1	1	2	1	1
Thus, the minimum total cost is 4 + 1 + 1 = 6.
```
 

**Constraints:**

* `1 <= n <= 500`

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 10.88 MB, Beats 6.76%
```
```c++
class Solution {
public:
    int minCost(int n) {
        int a;
        vector<int> dp(1024);
        dp[2] = 1;
        for (a = 3; a <= n; a ++) {
            dp[a] = (a / 2) * (a - a / 2) + dp[a / 2] + dp[a - a / 2];
        }
        return dp[n];
    }
};
```

**Solution 2: (Math)**

Intuition
Multiplying by 1 is always smaller
Approach
Any number x, if it is partioned as a + b, where a + b = x
Always taking the value of a as 1 gives a * b as a smallest multiple
For Example 6 can be partioned as
1 + 5 (1 * 5 = 5)
2 + 4 (2 * 4 = 8)
3 + 3 (3 * 3 = 9)
So multiplying by 1 is always smaller
If you taking 1 digit as 1, then you are summing up till n - 1
So 1 + 2 + 3 + 4 + 5 = 15, which is n * (n - 1) / 2
6 * (5) / 2 = 3 * 5 = 15
Example
For n = 4
1 + 3 = 4
For 3
1 + 2 = 3
For 2
1 + 1 = 2
Now summing up all these gives
1 + 2 + 3 = 6
Answer for 4 is 6
Complexity
Time complexity:
O(1)

Space complexity:
O(1)

                     cost
       6
     /   \
    1     5          1*5
         / \
        1   4        1*4
           / \
          1   3      1*3
             / \
            1   2    1*2
               / \
              1   1  1*1 
          

```
Runtime: 0 ms, Beats 100.00%
Memory: 8.29 MB, Beats 28.15%
```
```c++
class Solution {
public:
    int minCost(int n) {
        return n * (n - 1) / 2;
    }
};
```
