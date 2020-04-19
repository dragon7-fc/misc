1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K

Given the number `k`, return the minimum number of Fibonacci numbers whose sum is equal to `k`, whether a Fibonacci number could be used multiple times.

The Fibonacci numbers are defined as:

* F1 = 1
* F2 = 1
* Fn = Fn-1 + Fn-2 , for n > 2.

It is guaranteed that for the given constraints we can always find such fibonacci numbers that sum `k`.
 

**Example 1:**
```
Input: k = 7
Output: 2 
Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ... 
For k = 7 we can use 2 + 5 = 7.
```

**Example 2:**
```
Input: k = 10
Output: 2 
Explanation: For k = 10 we can use 2 + 8 = 10.
```

**Example 3:**
```
Input: k = 19
Output: 3 
Explanation: For k = 19 we can use 1 + 5 + 13 = 19.
```

**Constraints:**

* `1 <= k <= 10^9`

# Submissions
---
**Solution 1: (Greedy)**

**Intuition**

* We greedily substract the biggest fibonacci number `x` from `k`, and recursive to find the result for `k - x`.
* Then `f(k) = f(k - x) + 1`

```
Runtime: 32 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        res, a, b = 0, 1, 1
        while b <= k:
            a, b = b, a + b
        while a > 0:
            if a <= k:
                k -= a
                res += 1
            a, b = b - a, a
        return res
```