3109. Find the Index of Permutation

Given an array perm of length `n` which is a permutation of `[1, 2, ..., n]`, return the index of perm in the **lexicographically sorted**  array of all of the permutations of `[1, 2, ..., n]`.

Since the answer may be very large, return it modulo `10^9 + 7`.

 

**Example 1:**
```
Input: perm = [1,2]

Output: 0

Explanation:

There are only two permutations in the following order:

[1,2], [2,1]

And [1,2] is at index 0.
```

**Example 2:**
```
Input: perm = [3,1,2]

Output: 4

Explanation:

There are only six permutations in the following order:

[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]

And [3,1,2] is at index 4.
```
 

**Constraints:**

* `1 <= n == perm.length <= 105`
* `perm` is a permutation of `[1, 2, ..., n]`.

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 2909 ms
Memory: 26.77 MB
```
```c++
class Solution:
    def getPermutationIndex(self, perm: List[int]) -> int:
        res = 0
        cur = 1 # keep track of factorial
        M = 1000000007
        s = []
        for val in perm[::-1]:
            bisect.insort(s, val)
            idx = bisect.bisect_left(s, val)
            res = (res+idx*cur)%M
            cur = (cur*len(s))%M
        return res
```
