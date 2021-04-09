1551. Minimum Operations to Make Array Equal

You have an array `arr` of length `n` where `arr[i] = (2 * i) + 1` for all valid values of `i` (i.e. `0 <= i < n`).

In one operation, you can select two indices `x` and `y` where `0 <= x, y < n` and subtract `1` from `arr[x]` and add `1` to `arr[y]` (i.e. perform `arr[x] -=1` and `arr[y] += 1`). The goal is to make all the elements of the array equal. It is guaranteed that all the elements of the array can be made equal using some operations.

Given an integer `n`, the length of the array. Return the minimum number of operations needed to make all the elements of `arr` equal.

 

**Example 1:**
```
Input: n = 3
Output: 2
Explanation: arr = [1, 3, 5]
First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].
```

**Example 2:**
```
Input: n = 6
Output: 9
```

**Constraints:**

* `1 <= n <= 10^4`

# Submissions
---
**Solution 1: (Array)**
```
Runtime: 68 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def minOperations(self, n: int) -> int:
        op = 0
        odd = 1
        while odd < n:
            op += n - odd
            odd += 2
        return op
```

**Solution 2: (Math)**

it is really either one of the two series depending on the parity of `n`
`1+3+5+...+(n-1)` or `2+4+6+...+(n-1)`

```
Runtime: 32 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def minOperations(self, n: int) -> int:
        return (n+1)*(n-1)//4 if n%2 else n*n//4
```

**Solution 3: (Math)**
```
Runtime: 32 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def minOperations(self, n: int) -> int:
        last = 2*(n-1) + 1
        mid = (last+1)//2
        if n%2:
            return (last-mid) * ((n+1)//2) // 2
        else:
            return (1 + last-mid) * n//2 // 2
```