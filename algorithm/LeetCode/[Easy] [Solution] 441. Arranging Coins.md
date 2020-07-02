441. Arranging Coins

You have a total of `n` coins that you want to form in a staircase shape, where every `k`-th row must have exactly `k` coins.

Given `n`, find the total number of **full** staircase rows that can be formed.

`n` is a non-negative integer and fits within the range of a 32-bit signed integer.

**Example 1:**
```
n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
```

**Example 2:**
```
n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
```

# Solution
---
## Approach 1: Binary Search
This question is easy in a sense that one could run an **exhaustive iteration** to obtain the result. That could work, except that it would run out of time when the input becomes too large. So let us take a step back to look at the problem, before rushing to the implementation.

Assume that the answer is $k$, i.e. we've managed to complete $k$ rows of coins. These completed rows contain in total $1 + 2 + ... + k = \frac{k (k + 1)}{2}$ coins.

We could now reformulate the problem as follows:

>Find the maximum $k$ such that $\frac{k (k + 1)}{2} \le N$.

The problem seems to be one of those search problems. And instead of naive iteration, one could resort to another more efficient algorithm called binary search, as we can find in another similar problem called search insert position.

**Implementation**

```python
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            k = (right + left) // 2
            curr = k * (k + 1) // 2
            if curr == n:
                return k
            if n < curr:
                right = k - 1
            else:
                left = k + 1
        return right
```

**Complexity Analysis**

* Time complexity : $\mathcal{O}(\log N)$.

* Space complexity : $\mathcal{O}(1)$.

## Approach 2: Math
If we look deeper into the formula of the problem, we could actually solve it with the help of mathematics, without using any iteration.

As a reminder, the constraint of the problem can be expressed as follows:

$k(k + 1) \le 2N$

This could be solved by completing the square technique,

$\left(k + \frac{1}{2}\right)^2 - \frac{1}{4} \le 2N$

that results in the following answer:

$k = \left[\sqrt{2N + \frac{1}{4}} - \frac{1}{2}\right]$

**Implementation**

```python
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return (int)((2 * n + 0.25)**0.5 - 0.5)
```
**Complexity Analysis**

* Time complexity : $\mathcal{O}(1)$.

* Space complexity : $\mathcal{O}(1)$.

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 44 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            k = (right + left) // 2
            curr = k * (k + 1) // 2
            if curr == n:
                return k
            if n < curr:
                right = k - 1
            else:
                left = k + 1
        return right
```

**Solution 2: (Math)**
```
Runtime: 104 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return (int)((2 * n + 0.25)**0.5 - 0.5)
```

**Solution 3: (Binary Search)**
```
Runtime: 0 ms
Memory Usage: 5.9 MB
```
```c++
class Solution {
public:
    int arrangeCoins(int n) {
        long long int left = 0, right = n, k, curr;
        while (left <= right) {
            k = left + (right-left)/2;
            curr = (k * (k+1))/2;
            if (curr == n)
            {
                return k;
            }
            else if (n < curr)
            {
                right = k - 1;
            }
            else
            {
                left = k + 1;
            }
        }
        return right;
    }
};
```