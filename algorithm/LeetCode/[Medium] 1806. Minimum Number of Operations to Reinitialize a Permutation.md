1806. Minimum Number of Operations to Reinitialize a Permutation

You are given an **even** integer `n`. You initially have a permutation `perm` of size `n` where `perm[i] == i` (`0`-indexed).

In one operation, you will create a new array `arr`, and for each `i`:

* If `i % 2 == 0`, then `arr[i] = perm[i / 2]`.
* If `i % 2 == 1`, then `arr[i] = perm[n / 2 + (i - 1) / 2]`.

You will then assign `arr` to `perm`.

Return the minimum non-zero number of operations you need to perform on perm to return the permutation to its initial value.

 

**Example 1:**
```
Input: n = 2
Output: 1
Explanation: perm = [0,1] initially.
After the 1st operation, perm = [0,1]
So it takes only 1 operation.
```

**Example 2:**
```
Input: n = 4
Output: 2
Explanation: perm = [0,1,2,3] initially.
After the 1st operation, perm = [0,2,1,3]
After the 2nd operation, perm = [0,1,2,3]
So it takes only 2 operations.
```

**Example 3:**
```
Input: n = 6
Output: 4
```

**Constraints:**

* `2 <= n <= 1000`
* `n` is even.

# Submissions
---
**Solution 1: (Simulation)**
```
Runtime: 568 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        A, init = range(n), list(range(n))
        res = 0
        while res == 0 or A != init:
            A = [A[i // 2] if i % 2 == 0 else A[n // 2 + (i - 1) // 2] for i in range(n)]
            res += 1
        return res
```

**Solution 2: Simulation an index**

Find the inverse path of `i`.

```
Runtime: 0 ms
Memory Usage: 5.9 MB
```
```c++
class Solution {
public:
    int reinitializePermutation(int n) {
        int res = 0, i = 1;
        while (res == 0 || i > 1) {
            if (i < n / 2)
                i *= 2;
            else
                i = (i - n / 2) * 2 + 1;
            res++;
        }
        return res;
    }
};
```