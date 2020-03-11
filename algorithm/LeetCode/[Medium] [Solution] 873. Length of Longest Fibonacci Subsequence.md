873. Length of Longest Fibonacci Subsequence

A sequence `X_1, X_2, ..., X_n` is fibonacci-like if:

* `n >= 3`
* `X_i + X_{i+1} = X_{i+2} for all i + 2 <= n`

Given a **strictly increasing** array `A` of positive integers forming a sequence, find the **length** of the longest fibonacci-like subsequence of `A`.  If one does not exist, return 0.

(Recall that a subsequence is derived from another sequence A by deleting any number of elements (including none) from A, without changing the order of the remaining elements.  For example, `[3, 5, 8]` is a subsequence of `[3, 4, 5, 6, 7, 8]`.)

 

**Example 1:**
```
Input: [1,2,3,4,5,6,7,8]
Output: 5
Explanation:
The longest subsequence that is fibonacci-like: [1,2,3,5,8].
```

**Example 2:**
```
Input: [1,3,7,11,12,14,18]
Output: 3
Explanation:
The longest subsequence that is fibonacci-like:
[1,11,12], [3,11,14] or [7,11,18].
```

**Note:**

* `3 <= A.length <= 1000`
* `1 <= A[0] < A[1] < ... < A[A.length - 1] <= $10^9$`
(The time limit has been reduced by 50% for submissions in Java, C, and C++.)

# Solution
---
## Approach 1: Brute Force with Set
**Intuition**

Every Fibonacci-like subsequence has each two adjacent terms determine the next expected term. For example, with 2, 5, we expect that the sequence must continue 7, 12, 19, 31, etc.

We can use a `Set` structure to determine quickly whether the next term is in the array `A` or not. Because of the exponential growth of these terms, there are at most 43 terms in any Fibonacci-like subsequence that has maximum value $\leq 10^9$.

**Algorithm**

For each starting pair `A[i]`, `A[j]`, we maintain the next expected value `y = A[i] + A[j]` and the previously seen largest value `x = A[j]`. If `y` is in the array, then we can then update these values `(x, y) -> (y, x+y)`.

Also, because subsequences are only fibonacci-like if they have length 3 or more, we must perform the check `ans >= 3 ? ans : 0` at the end.

```python
class Solution(object):
    def lenLongestFibSubseq(self, A):
        S = set(A)
        ans = 0
        for i in xrange(len(A)):
            for j in xrange(i+1, len(A)):
                """
                With the starting pair (A[i], A[j]),
                y represents the future expected value in
                the fibonacci subsequence, and x represents
                the most current value found.
                """
                x, y = A[j], A[i] + A[j]
                length = 2
                while y in S:
                    x, y = y, x + y
                    length += 1
                ans = max(ans, length)
        return ans if ans >= 3 else 0
```

**Complexity Analysis**

* Time Complexity: $O(N^2 \log M)$, where $N$ is the length of `A`, and $M$ is the maximum value of `A`.

* Space Complexity: $O(N)$, the space used by the set `S`.

## Approach 2: Dynamic Programming
**Intuition**

Think of two consecutive terms `A[i]`, `A[j]` in a fibonacci-like subsequence as a single node `(i, j)`, and the entire subsequence is a path between these consecutive nodes. For example, with the fibonacci-like subsequence `(A[1] = 2, A[2] = 3, A[4] = 5, A[7] = 8, A[10] = 13)`, we have the path between nodes `(1, 2) <-> (2, 4) <-> (4, 7) <-> (7, 10)`.

The motivation for this is that two nodes `(i, j)` and `(j, k)` are connected if and only if `A[i] + A[j] == A[k]`, and we needed this amount of information to know about this connection. Now we have a problem similar to Longest Increasing Subsequence.

**Algorithm**

Let `longest[i, j]` be the longest path ending in `[i, j]`. Then `longest[j, k] = longest[i, j] + 1` if `(i, j)` and `(j, k)` are connected. Since `i` is uniquely determined as `A.index(A[k] - A[j])`, this is efficient: we check for each `j < k` what `i` is potentially, and update `longest[j, k]` accordingly.

```python
class Solution(object):
    def lenLongestFibSubseq(self, A):
        index = {x: i for i, x in enumerate(A)}
        longest = collections.defaultdict(lambda: 2)

        ans = 0
        for k, z in enumerate(A):
            for j in xrange(k):
                i = index.get(z - A[j], None)
                if i is not None and i < j:
                    cand = longest[j, k] = longest[i, j] + 1
                    ans = max(ans, cand)

        return ans if ans >= 3 else 0
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the length of `A`.

* Space Complexity: $O(N \log M)$, where $M$ is the largest element of `A`. We can show that the number of elements in a subsequence is bounded by $O(\log \frac{M}{a})$ where $a$ is the minimum element in the subsequence.

# Submissions
---
**Solution: (Dynamic Programming)**
```
Runtime: 924 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        index = {x: i for i, x in enumerate(A)}
        longest = collections.defaultdict(lambda: 2)

        ans = 0
        for k, z in enumerate(A):
            for j in range(k):
                i = index.get(z - A[j], None)
                if i is not None and i < j:
                    cand = longest[j, k] = longest[i, j] + 1
                    ans = max(ans, cand)

        return ans if ans >= 3 else 0
```

**Solution 1: (DFS)**
```
Runtime: 480 ms
Memory Usage: 13.5 MB
```
```python
class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        ans = 0
        index = {x: i for i, x in enumerate(A)}
        
        def dfs(idx, path):
            nonlocal ans
            a, b = path[-2], path[-1]
            c = a+b
            if c in index:
                k = index[c]
                ans = max(ans, len(path) + 1)
                dfs(k+1, path + [c])
                    
        for i, a in enumerate(A):
            for j, b in enumerate(A[i+1:]):
                if a + b in index:
                    k = index[a+b]
                    dfs(k, [a, b])
                        
        return ans
```