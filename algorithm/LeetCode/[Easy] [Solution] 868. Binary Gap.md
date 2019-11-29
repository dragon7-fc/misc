868. Binary Gap

Given a positive integer `N`, find and return the longest distance between two consecutive 1's in the binary representation of `N`.

If there aren't two consecutive 1's, return 0.

 

**Example 1:**
```
Input: 22
Output: 2
Explanation: 
22 in binary is 0b10110.
In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
The first consecutive pair of 1's have distance 2.
The second consecutive pair of 1's have distance 1.
The answer is the largest of these two distances, which is 2.
```

**Example 2:**
```
Input: 5
Output: 2
Explanation: 
5 in binary is 0b101.
```

**Example 3:**
```
Input: 6
Output: 1
Explanation: 
6 in binary is 0b110.
```

**Example 4:**
```
Input: 8
Output: 0
Explanation: 
8 in binary is 0b1000.
There aren't any consecutive pairs of 1's in the binary representation of 8, so we return 0.
``` 

**Note:**

* `1 <= N <= 10^9`

# Solution
---
## Approach 1: Store Indexes
**Intuition**

Since we wanted to inspect the distance between consecutive 1s in the binary representation of `N`, let's write down the index of each `1` in that binary representation. For example, if `N = 22 = 0b10110`, then we'll write `A = [1, 2, 4]`. This makes it easier to proceed, as now we have a problem about adjacent values in an array.

**Algorithm**

Let's make a list `A` of indices `i` such that `N` has the `i`th bit set.

With this array A, finding the maximum distance between consecutive `1`s is much easier: it's the maximum distance between adjacent values of this array.

```python
class Solution(object):
    def binaryGap(self, N):
        A = [i for i in xrange(32) if (N >> i) & 1]
        if len(A) < 2: return 0
        return max(A[i+1] - A[i] for i in xrange(len(A) - 1))
```

**Complexity Analysis**

* Time Complexity: $O(\log N)$. Note that $\log N$ is the number of digits in the binary representation of $N$.

* Space Complexity: $O(\log N)$, the space used by A.

## Approach 2: One Pass
**Intuition**

In Approach 1, we created an array `A` of indices `i` for which `N` had the `i`th bit set.

Since we only care about consecutive values of this array `A`, we don't need to store the whole array. We only need to remember the last value seen.

**Algorithm**

We'll store last, the last value added to the virtual array `A`. If `N` has the `i`th bit set, a candidate answer is `i - last`, and then the new last value added to `A` would be `last = i`.

```python
class Solution(object):
    def binaryGap(self, N):
        last = None
        ans = 0
        for i in xrange(32):
            if (N >> i) & 1:
                if last is not None:
                    ans = max(ans, i - last)
                last = i
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(\log N)$. Note that $\log N$ is the number of digits in the binary representation of $N$.

* Space Complexity: $O(1)$.

# Submissions
---
**Solution 1:**
```
Runtime: 24 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def binaryGap(self, N: int) -> int:
        last = None
        ans = 0
        for i in range(32):
            if (N >> i) & 1:
                if last is not None:
                    ans = max(ans, i - last)
                last = i
        return ans
```