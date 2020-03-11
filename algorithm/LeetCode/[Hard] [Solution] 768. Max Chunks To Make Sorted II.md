768. Max Chunks To Make Sorted II

This question is the same as "Max Chunks to Make Sorted" except the integers of the given array are not necessarily distinct, the input array could be up to length `2000`, and the elements could be up to `10**8`.

Given an array `arr` of integers (**not necessarily distinct**), we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

**Example 1:**
```
Input: arr = [5,4,3,2,1]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.
```

**Example 2:**
```
Input: arr = [2,1,3,4,4]
Output: 4
Explanation:
We can split into two chunks, such as [2, 1], [3, 4, 4].
However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.
```

**Note:**

* `arr` will have length in range `[1, 2000]`.
* `arr[i]` will be an integer in range `[0, 10**8]`.

# Solution
---
## Approach #1: Sliding Window [Accepted]
**Intuition**

Let's try to find the smallest left-most chunk.

**Algorithm**

Notice that if $a_1, a_2, \dots, a_m$ is a chunk, and $a_1, a_2, \dots, a_n$ is a chunk ($m < n$), then $a_{m+1}, a_{m+2}, \dots, a_n$ is a chunk too. This shows that a greedy approach produces the highest number of chunks.

We know the array `arr` should end up like `expect = sorted(arr)`. If the count of the first `k` elements minus the count what those elements should be is zero everywhere, then the first k elements form a valid chunk. We repeatedly perform this process.

We can use a variable `nonzero` to count the number of letters where the current count is non-zero.

```python
class Solution(object):
    def maxChunksToSorted(self, arr):
        count = collections.defaultdict(int)
        ans = nonzero = 0

        for x, y in zip(arr, sorted(arr))
            count[x] += 1
            if count[x] == 0: nonzero -= 1
            if count[x] == 1: nonzero += 1

            count[y] -= 1
            if count[y] == -1: nonzero += 1
            if count[y] == 0: nonzero -= 1

            if nonzero == 0: ans += 1

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N \log N)$, where $N$ is the length of `arr`

* Space Complexity: $O(N)$.

## Approach #2: Sorted Count Pairs [Accepted]
**Intuition**

As in Approach #1, let's try to find the smallest left-most chunk, where we have some expectation `expect = sorted(arr)`

If the elements were distinct, then it is enough to find the smallest `k` with `max(arr[:k+1]) == expect[k]`, as this must mean the elements of `arr[:k+1]` are some permutation of `expect[:k+1]`.

Since the elements are not distinct, this fails; but we can amend the cumulative multiplicity of each element to itself to make the elements distinct.

**Algorithm**

Instead of elements `x`, have counted elements `(x, count)` where count ranges from `1` to the total number of `x` present in `arr`.

Now `cur` will be the cumulative maximum of `counted[:k+1]`, where we expect a result of `Y = expect[k]`. We count the number of times they are equal.

```python
class Solution(object):
    def maxChunksToSorted(self, arr):
        count = collections.Counter()
        counted = []
        for x in arr:
            count[x] += 1
            counted.append((x, count[x]))

        ans, cur = 0, None
        for X, Y in zip(counted, sorted(counted)):
            cur = max(cur, X)
            if cur == Y:
                ans += 1
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N \log N)$, where $N$ is the length of `arr`

* Space Complexity: $O(N)$.

# Submissions
---
**Solution 1: (Sliding Window)**
```
Runtime: 80 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count = collections.defaultdict(int)
        ans = nonzero = 0

        for x, y in zip(arr, sorted(arr)):
            count[x] += 1
            if count[x] == 0: nonzero -= 1
            if count[x] == 1: nonzero += 1

            count[y] -= 1
            if count[y] == -1: nonzero += 1
            if count[y] == 0: nonzero -= 1

            if nonzero == 0: ans += 1

        return ans
```

**Solution 2: (Sorted Count Pairs)**
```
Runtime: 92 ms
Memory Usage: 13.1 MB
```
```python
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count = collections.Counter()
        counted = []
        for x in arr:
            count[x] += 1
            counted.append((x, count[x]))

        ans, cur = 0, None
        for X, Y in zip(counted, sorted(counted)):
            cur = max(cur, X) if cur else X
            if cur == Y:
                ans += 1
        return ans
```