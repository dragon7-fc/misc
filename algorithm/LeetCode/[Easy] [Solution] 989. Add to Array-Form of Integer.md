989. Add to Array-Form of Integer

For a non-negative integer `X`, the array-form of X is an array of its digits in left to right order.  For example, if `X = 1231`, then the array form is `[1,2,3,1]`.

Given the array-form `A` of a non-negative integer `X`, return the array-form of the integer `X+K`.

 

**Example 1:**
```
Input: A = [1,2,0,0], K = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
```

**Example 2:**
```
Input: A = [2,7,4], K = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
```

**Example 3:**
```
Input: A = [2,1,5], K = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
```

**Example 4:**
```
Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
Output: [1,0,0,0,0,0,0,0,0,0,0]
Explanation: 9999999999 + 1 = 10000000000
``` 

**Note：**

1. 1 <= `A.length` <= 10000
1. 0 <= `A[i]` <= 9
1. 0 <= `K` <= 10000
1. If `A.length` > 1, then `A[0]` != 0

# Solution
---
## Approach 1: Schoolbook Addition
**Intuition**

Let's add numbers in a schoolbook way, column by column. For example, to add `123` and `912`, we add `3+2`, then `2+1`, then `1+9`. Whenever our addition result is more than `10`, we carry the `1` into the next column. The result is `1035`.

**Algorithm**

We can do a variant of the above idea that is easier to implement - we put the entire addend in the first column from the right.

Continuing the example of `123 + 912`, we start with `[1, 2, 3+912]`. Then we perform the addition `3+912`, leaving `915`. The 5 stays as the digit, while we `'carry' 910` into the next column which becomes `91`.

We repeat this process with `[1, 2+91, 5]`. We have `93`, where `3` stays and `90` is carried over as `9`. Again, we have `[1+9, 3, 5]` which transforms into `[1, 0, 3, 5]`.

```python
class Solution(object):
    def addToArrayForm(self, A, K):
        A[-1] += K
        for i in xrange(len(A) - 1, -1, -1):
            carry, A[i] = divmod(A[i], 10)
            if i: A[i-1] += carry
        if carry:
            A = map(int, str(carry)) + A
        return A
```

**Complexity Analysis**

* Time Complexity: $O(\max(N, \log K))$ where $N$ is the length of `A`.

* Space Complexity: $O(\max(N, \log K))$.

# Submissions
---
**Solution 1:**
```
Runtime: 356 ms
Memory Usage: 14.8 MB
```
```python
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        return list(str(int(''.join(map(str, A)))+K))
```