952. Largest Component Size by Common Factor

Given a non-empty array of unique positive integers `A`, consider the following graph:

* There are `A.length` nodes, labelled `A[0]` to `A[A.length - 1]`;
* There is an edge between `A[i]` and `A[j]` if and only if `A[i]` and `A[j]` share a common factor greater than `1`.

Return the size of the largest connected component in the `graph`.

 

**Example 1:**
```
Input: [4,6,15,35]
Output: 4
```

**Example 2:**
```
Input: [20,50,9,63]
Output: 2
```

**Example 3:**
```
Input: [2,3,6,7,4,12,21,39]
Output: 8
```

**Note:**

* `1 <= A.length <= 20000`
* `1 <= A[i] <= 100000`

# Solution
---
## Approach 1: Union-Find
We will skip the explanation of how a DSU structure is implemented. Please refer to https://leetcode.com/problems/redundant-connection/solution/ for a tutorial on DSU.

**Intuition**

Let $W = \max(A[i])$, and $R = \sqrt{W}$. For each value $A[i]$, there is at most one prime factor $p \geq R$ dividing $A[i]$. Let's call $A[i]$'s "big prime" this $p$, if it exists.

This means that there are at most $R + A\text{.length}$ unique prime divisors of elements in $A$: the big primes correspond to a maximum of $A\text{.length}$ values, and the small primes are all less than $R$, so there's at most $R$ of them too.

**Algorithm**

Factor each $A[i]$ into prime factors, and index every occurrence of these primes. (To save time, we can use a sieve. Please see this article's comments for more details.)

Then, use a union-find structure to union together any prime factors that came from the same $A[i]$.

Finally, we can count the size of each component, by inspecting and counting the id of the component each $A[i]$ belongs to.

```python
class DSU:
    def __init__(self, N):
        self.p = range(N)

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

class Solution(object):
    def largestComponentSize(self, A):
        B = []
        for x in A:
            facs = []
            d = 2
            while d * d <= x:
                if x % d == 0:
                    while x % d == 0:
                        x /= d
                    facs.append(d)
                d += 1

            if x > 1 or not facs:
                facs.append(x)
            B.append(facs)

        primes = list({p for facs in B for p in facs})
        prime_to_index = {p: i for i, p in enumerate(primes)}

        dsu = DSU(len(primes))
        for facs in B:
            for x in facs:
                dsu.union(prime_to_index[facs[0]], prime_to_index[x])

        count = collections.Counter(dsu.find(prime_to_index[facs[0]]) for facs in B)
        return max(count.values())
```

**Complexity Analysis**

* Time Complexity: $O(N\sqrt{W})$ where $N$ is the length of A, and $W = \max(A[i])$.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution 1: (Union-Find)**
```
Runtime: 2984 ms
Memory Usage: 17.4 MB
```
```python
class DSU:
    def __init__(self, N):
        self.p = [_ for _ in range(N)]

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        B = []
        for x in A:
            facs = []
            d = 2
            while d * d <= x:
                if x % d == 0:
                    while x % d == 0:
                        x /= d
                    facs.append(d)
                d += 1

            if x > 1 or not facs:
                facs.append(x)
            B.append(facs)

        primes = list({p for facs in B for p in facs})
        prime_to_index = {p: i for i, p in enumerate(primes)}

        dsu = DSU(len(primes))
        for facs in B:
            for x in facs:
                dsu.union(prime_to_index[facs[0]], prime_to_index[x])

        count = collections.Counter(dsu.find(prime_to_index[facs[0]]) for facs in B)
        return max(count.values())
```