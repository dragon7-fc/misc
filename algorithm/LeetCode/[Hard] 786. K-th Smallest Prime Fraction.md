786. K-th Smallest Prime Fraction

A sorted list `A` contains 1, plus some number of primes.  Then, for every `p < q` in the list, we consider the fraction `p/q`.

What is the `K`-th smallest fraction considered?  Return your answer as an array of ints, where `answer[0] = p` and `answer[1] = q`.

**Examples:**
```
Input: A = [1, 2, 3, 5], K = 3
Output: [2, 5]
Explanation:
The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
The third fraction is 2/5.
```

```
Input: A = [1, 7], K = 1
Output: [1, 7]
```

**Note:**

* `A` will have length between `2` and `2000`.
* Each `A[i]` will be between `1` and `30000`.
* `K` will be between `1` and `A.length * (A.length - 1) / 2`.

# Submissions
---
**Solution 1: (Heap)**
```
Runtime: 6828 ms
Memory Usage: 178.2 MB
```
```python
class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        visited = set((0, len(A) - 1))
        heap = [(float(A[0]) / A[-1], 0, len(A) - 1)]
        while K > 0:
            K -= 1
            val, i, j = heapq.heappop(heap)
            if i + 1 < j:
                if (i, j - 1) not in visited:
                    visited.add((i, j - 1))
                    heapq.heappush(heap,(float(A[i]) / A[j - 1], i, j - 1))
                if (i + 1, j) not in visited:
                    visited.add((i + 1, j))
                    heapq.heappush(heap,(float(A[i + 1]) / A[j],i + 1, j))
        return [A[i],A[j]]
```

**Solution 2: (Binary Search)**

* The answer must be between 0, 1. We use binary seach to check the exact upper bound.
* Then use bisect to check for this upper bound, what is the larget prime ratio.

* Complexicity (O(nlg n lg n))

Notice that the second part can be doen using sliding window, which reduce the total complexicity to (O(n lg n))

class Solution:

```
Runtime: 340 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        def count(tar):
            res,tmp = 0, [0,A[-1]]
            for i in range(len(A)):
                loc = bisect.bisect_left(A,A[i]/tar)
                res += len(A) - loc
                if loc < len(A) and A[i]/A[loc] > tmp[0]/tmp[1]:
                    tmp = [A[i],A[loc]]
            return res, tmp
        l, m, r = 0, 0.5,1
        cur,_ = count(m)
        while cur != K:
            if cur < K:
                l = m
            else:
                r = m
            m = (l+r)/2
            cur, _ = count(m)
        return _
```