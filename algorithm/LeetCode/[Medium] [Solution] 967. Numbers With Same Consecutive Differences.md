967. Numbers With Same Consecutive Differences

Return all **non-negative** integers of length `N` such that the absolute difference between every two consecutive digits is K.

Note that **every** number in the answer **must** not have leading zeros **except** for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.

 

**Example 1:**

```
Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
```

**Example 2:**

```
Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
```

**Note:**

1. `1 <= N <= 9`
1. `0 <= K <= 9`

# Solution
---
## Approach 1: Brute Force
**Intuition**

Let's try to write some number in the answer digit by digit.

For each digit except the first, there are at most `2` choices for that digit. This means that there are at most $9 * 2^8$ possible `9` digit numbers, for example. This is small enough to brute force.

**Algorithm**

An $N$ digit number is just an $N-1$ digit number with a final digit added. If the $N-1$ digit number ends in a digit $d$, then the $N$ digit number will end in $d-K$ or d+Kd+K (provided these are digits in the range $[0,9]$). We store these numbers in a Set structure to avoid duplicates.

Also, we should be careful about leading zeroes -- only 1 digit numbers will start with `0`.

```python
class Solution(object):
    def numsSameConsecDiff(self, N, K):
        ans = {x for x in range(1, 10)}
        for _ in xrange(N-1):
            ans2 = set()
            for x in ans:
                d = x % 10
                if d - K >= 0:
                    ans2.add(10*x + d-K)
                if d + K <= 9:
                    ans2.add(10*x + d+K)
            ans = ans2

        if N == 1:
            ans.add(0)

        return list(ans)
```

**Complexity Analysis**

* Time Complexity: $O(2^N)$.

* Space Complexity: $O(2^N)$.

# Submissions
---
**Solution:**
```
Runtime: 40 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        ans = {x for x in range(1, 10)}
        for _ in range(N-1):
            ans2 = set()
            for x in ans:
                d = x % 10
                if d - K >= 0:
                    ans2.add(10*x + d-K)
                if d + K <= 9:
                    ans2.add(10*x + d+K)
            ans = ans2

        if N == 1:
            ans.add(0)

        return list(ans)
```