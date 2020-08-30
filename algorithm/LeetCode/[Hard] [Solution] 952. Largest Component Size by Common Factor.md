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

**Solution 2: (Union-Find via Factors)**
```
Runtime: 2452 ms
Memory Usage: 20.1 MB
```
```python
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        
        dsu = DisjointSetUnion(max(A))

        # attribute each element in A
        #   to all the groups that lead by its factors.
        for a in A:
            for factor in range(2, int(sqrt(a))+1):
                if a % factor == 0:
                    dsu.union(a, factor)
                    dsu.union(a, a // factor)

        # count the size of group one by one
        max_size = 0
        group_count = defaultdict(int)
        for a in A:
            group_id = dsu.find(a)
            group_count[group_id] += 1
            max_size = max(max_size, group_count[group_id])

        return max_size


class DisjointSetUnion(object):

    def __init__(self, size):
        # initially, each node is an independent component
        self.parent = [i for i in range(size+1)]
        # keep the size of each component
        self.size = [1] * (size+1)
    
    def find(self, x):
        """ return the component id that the element x belongs to. """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """ merge the two components that x, y belongs to respectively,
              and return the merged component id as the result.
        """
        px, py = self.find(x), self.find(y)
        
        # the two nodes share the same set
        if px == py:
            return px
        
        # otherwise, connect the two sets (components)
        if self.size[px] > self.size[py]:
            # add the node to the union with less members.
            # keeping px as the index of the smaller component
            px, py = py, px
        # add the smaller component to the larger one
        self.parent[px] = py
        self.size[py] += self.size[px]
        # return the final (merged) group
        return py
```

**Solution 3: (Union-Find via Factors)**
```
Runtime: 2820 ms
Memory Usage: 20.8 MB
```
```python
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        
        dsu = DisjointSetUnion(max(A))
        num_factor_map = {}
        
        for num in A:
            prime_factors = list(set(self.primeDecompose(num)))
            # map a number to its first prime factor
            num_factor_map[num] = prime_factors[0]
            # merge all groups that contain the prime factors.
            for i in range(0, len(prime_factors)-1):
                dsu.union(prime_factors[i], prime_factors[i+1])
        
        max_size = 0
        group_count = defaultdict(int)
        for num in A:
            group_id = dsu.find(num_factor_map[num])
            group_count[group_id] += 1
            max_size = max(max_size, group_count[group_id]) 
        
        return max_size


    def primeDecompose(self, num):
        """ decompose any positive number into 
                a series of prime factors.
            e.g. 12 = 2 * 2 * 3
        """
        factor = 2
        prime_factors = []
        while num >= factor * factor:
            if num % factor == 0:
                prime_factors.append(factor)
                num = num // factor
            else:
                factor += 1
        prime_factors.append(num)
        return prime_factors


class DisjointSetUnion(object):

    def __init__(self, size):
        # initially, each node is an independent component
        self.parent = [i for i in range(size+1)]
        # keep the size of each component
        self.size = [1] * (size+1)
    
    def find(self, x):
        """ return the component id that the element x belongs to. """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """ merge the two components that x, y belongs to respectively,
              and return the merged component id as the result.
        """
        px, py = self.find(x), self.find(y)
        
        # the two nodes share the same set
        if px == py:
            return px
        
        # otherwise, connect the two sets (components)
        if self.size[px] > self.size[py]:
            # add the node to the union with less members.
            # keeping px as the index of the smaller component
            px, py = py, px
        # add the smaller component to the larger one
        self.parent[px] = py
        self.size[py] += self.size[px]
        # return the final (merged) group
        return py
```