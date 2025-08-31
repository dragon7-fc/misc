3021. Alice and Bob Playing Flower Game

Alice and Bob are playing a turn-based game on a circular field surrounded by flowers. The circle represents the field, and there are `x` flowers in the clockwise direction between Alice and Bob, and `y` flowers in the anti-clockwise direction between them.

The game proceeds as follows:

1. Alice takes the first turn.
1. In each turn, a player must choose either the clockwise or anti-clockwise direction and pick one flower from that side.
1. At the end of the turn, if there are no flowers left at all, the **current** player captures their opponent and wins the game.

Given two integers, `n` and `m`, the task is to compute the number of possible pairs `(x, y)` that satisfy the conditions:

1. Alice must win the game according to the described rules.
1. The number of flowers `x` in the clockwise direction must be in the range `[1,n]`.
1. The number of flowers `y` in the anti-clockwise direction must be in the range `[1,m]`.

Return the number of possible pairs `(x, y)` that satisfy the conditions mentioned in the statement.

 

**Example 1:**
```
Input: n = 3, m = 2
Output: 3
Explanation: The following pairs satisfy conditions described in the statement: (1,2), (3,2), (2,1).
```

**Example 2:**
```
Input: n = 1, m = 1
Output: 0
Explanation: No pairs satisfy the conditions described in the statement.
```

**Constraints:**

* `1 <= n, m <= 10^5`

# Submissions
---
**Solution 1: (Math)**

Alice wins when x + y is odd. This happens when either:

* x is odd and y is even, or
* y is odd and x is even.

We can compute the number of such combinations in O(1):

* x is odd n / 2 + n % 2 times, and even m / 2 times.
* y is odd m / 2 + m % 2 times, and even n / 2 times.

So, the formula is m / 2 * (n / 2 + n % 2) + n / 2 * (m / 2 + m % 2), which (thanks heizit) is reduced to m * n / 2.

```
Runtime: 4 ms
Memory: 7.64 MB
```
```c++
class Solution {
public:
    long long flowerGame(int n, int m) {
        return (long long)m * n / 2;
    }
};
```

**Solution 2: (Math)**

There are n * m total possible pairs. Exactly half of them will have different parity (one odd, one even). Therefore the answer is n * m / 2.

```
Runtime: 0 ms, Beats 100.00%
Memory: 8.42 MB, Beats 48.89%
```
```c++
class Solution {
public:
    long long flowerGame(int n, int m) {
        return (long long)n*m/2;
    }
};
```
