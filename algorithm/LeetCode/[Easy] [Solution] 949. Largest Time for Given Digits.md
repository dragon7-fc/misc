949. Largest Time for Given Digits

Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

 

**Example 1:**
```
Input: [1,2,3,4]
Output: "23:41"
```

**Example 2:**
```
Input: [5,5,5,5]
Output: ""
```

**Note:**

1. `A.length == 4`
1. `0 <= A[i] <= 9`

# Solution
---
## Approach 1: Brute Force
**Intuition**

Try all possible times, and remember the largest one.

**Algorithm (Java)**

Iterate over all permutations `(i, j, k, l)` of `(0, 1, 2, 3)`. For each permutation, we can try the time `A[i]A[j] : A[k]A[l]`.

This is a valid time if and only if the number of hours `10*A[i] + A[j]` is less than `24`; and the number of minutes `10*A[k] + A[l]` is less than `60`.

We will output the largest valid time.

**Algorithm (Python)**

For each possible ordering of the 4 digits, if it's a legal time and the time is greater than the one we have stored, update the answer.

```python
class Solution(object):
    def largestTimeFromDigits(self, A):
        ans = -1
        for h1, h2, m1, m2 in itertools.permutations(A):
            hours = 10 * h1 + h2
            mins = 10 * m1 + m2
            time = 60 * hours + mins
            if 0 <= hours < 24 and 0 <= mins < 60 and time > ans:
                ans = time

        return "{:02}:{:02}".format(*divmod(ans, 60)) if ans >= 0 else ""
```

**Complexity Analysis**

* Time Complexity: $O(1)$.

* Space Complexity: $O(1)$.

# Submissions
---
**Solution:**
```
Runtime: 32 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        ans = -1
        for h1, h2, m1, m2 in itertools.permutations(A):
            hours = 10 * h1 + h2
            mins = 10 * m1 + m2
            time = 60 * hours + mins
            if 0 <= hours < 24 and 0 <= mins < 60 and time > ans:
                ans = time

        return "{:02}:{:02}".format(*divmod(ans, 60)) if ans >= 0 else ""
```