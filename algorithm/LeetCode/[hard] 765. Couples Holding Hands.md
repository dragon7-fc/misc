765. Couples Holding Hands

N couples sit in 2N seats arranged in a row and want to hold hands. We want to know the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing **any** two people, then they stand up and switch seats.

The people and seats are represented by an integer from `0` to `2N-1`, the couples are numbered in order, the first couple being `(0, 1)`, the second couple being `(2, 3)`, and so on with the last couple being `(2N-2, 2N-1)`.

The couples' initial seating is given by `row[i]` being the value of the person who is initially sitting in the `i`-th seat.

**Example 1:**
```
Input: row = [0, 2, 1, 3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.
```

**Example 2:**
```
Input: row = [3, 2, 0, 1]
Output: 0
Explanation: All couples are already seated side by side.
```

**Note:**

* `len(row)` is even and in the range of `[4, 60]`.
* `row` is guaranteed to be a permutation of `0...len(row)-1`.

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 24 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        N = len(row)
        def findswap(swapIndex, valueToFind):
            for j in range(swapIndex + 1, N):
                if row[j] == valueToFind:
                    self.count += 1
                    row[j], row[swapIndex] = row[swapIndex], row[j]
        i = 0
        self.count = 0
        while i < N:
            if row[i]%2 == 0:
                if row[i+1] != row[i] + 1:
                    findswap(i+1, row[i] + 1)
            else:
                if row[i+1] != row[i] - 1:
                    findswap(i+1, row[i] - 1)
            i += 2
        return self.count
```

**Solution 2: (Union Find)**
```
Runtime: 32 ms
Memory Usage: 12.7 MB
```
```python
class DSU(object):
    def __init__(self, n):
        self.count = n
        self.p = [_ for _ in range(n)]
    
    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        if xp == yp: return False
        self.count -= 1
        self.p[xp] = yp
        return True
    
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        N = len(row)
        dsu = DSU(N)

        for i in range(0, N, 2):
            dsu.union(i, i+1)
            dsu.union(row[i], row[i+1])
        
        return N//2 - dsu.count
```