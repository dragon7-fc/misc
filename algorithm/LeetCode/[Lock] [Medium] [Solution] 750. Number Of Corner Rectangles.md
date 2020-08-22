750. Number Of Corner Rectangles

Given a grid where each entry is only 0 or 1, find the number of corner rectangles.

A corner rectangle is 4 distinct 1s on the grid that form an axis-aligned rectangle. Note that only the corners need to have the value 1. Also, all four 1s used must be distinct.

 

**Example 1:**
```
Input: grid = 
[[1, 0, 0, 1, 0],
 [0, 0, 1, 0, 1],
 [0, 0, 0, 1, 0],
 [1, 0, 1, 0, 1]]
Output: 1
Explanation: There is only one corner rectangle, with corners grid[1][2], grid[1][4], grid[3][2], grid[3][4].
```

**Example 2:**
```
Input: grid = 
[[1, 1, 1],
 [1, 1, 1],
 [1, 1, 1]]
Output: 9
Explanation: There are four 2x2 rectangles, four 2x3 and 3x2 rectangles, and one 3x3 rectangle.
```

**Example 3:**
```
Input: grid = 
[[1, 1, 1, 1]]
Output: 0
Explanation: Rectangles must have four distinct corners.
```

# Solution
---
## Approach #1: Count Corners [Accepted]
**Intuition**

We ask the question: for each additional row, how many more rectangles are added?

For each pair of 1s in the new row (say at `new_row[i]` and `new_row[j])`, we could create more rectangles where that pair forms the base. The number of new rectangles is the number of times some previous row had `row[i] = row[j] = 1`.

**Algorithm**

Let's maintain a count `count[i, j]`, the number of times we saw `row[i] = row[j] = 1`. When we process a new row, for every pair `new_row[i] = new_row[j] = 1`, we add `count[i, j]` to the answer, then we increment `count[i, j]`.

```python
class Solution(object):
    def countCornerRectangles(self, grid):
        count = collections.Counter()
        ans = 0
        for row in grid:
            for c1, v1 in enumerate(row):
                if v1:
                    for c2 in xrange(c1+1, len(row)):
                        if row[c2]:
                            ans += count[c1, c2]
                            count[c1, c2] += 1
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(R*C^2)$ where $R, C$ is the number of rows and columns.

* Space Complexity: $O(C^2)$ in additional space.

## Approach #2: Heavy and Light Rows [Accepted]
**Intuition and Algorithm**

Can we improve on the ideas in Approach #1? When a row is filled with $X$ 1s, we do $O(X^2)$ work to enumerate every pair of 1s. This is okay when $X$ is small, but expensive when $X$ is big.

Say the entire top row is filled with 1s. When looking at the next row with say, f 1s that match the top row, the number of rectangles created is just the number of pairs of 1s, which is f * (f-1) / 2. We could find each f quickly using a Set and a simple linear scan of each row.

Let's call a row to be heavy if it has more than $\sqrt N$ points. The above algorithm changes the complexity of counting a heavy row from $O(C^2)$ to $O(N)$, and there are at most $\sqrt N$ heavy rows.

```python
class Solution(object):
    def countCornerRectangles(self, grid):
        rows = [[c for c, val in enumerate(row) if val]
                for row in grid]
        N = sum(len(row) for row in grid)
        SQRTN = int(N**.5)

        ans = 0
        count = collections.Counter()
        for r, row in enumerate(rows):
            if len(row) >= SQRTN:
                target = set(row)
                for r2, row2 in enumerate(rows):
                    if r2 <= r and len(row2) >= SQRTN:
                        continue
                    found = sum(1 for c2 in row2 if c2 in target)
                    ans += found * (found - 1) / 2
            else:
                for pair in itertools.combinations(row, 2):
                    ans += count[pair]
                    count[pair] += 1

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N \sqrt N + R*C)$ where $N$ is the number of ones in the grid.

* Space Complexity: $O(N + R + C^2)$ in additional space, for rows, target, and count.

# Submissions
---
**Solution 1: (Count Corners)**
```
Runtime: 1924 ms
Memory Usage: 16.8 MB
```
```python
class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        count = collections.Counter()
        ans = 0
        for row in grid:
            for c1, v1 in enumerate(row):
                if v1:
                    for c2 in range(c1+1, len(row)):
                        if row[c2]:
                            ans += count[c1, c2]
                            count[c1, c2] += 1
        return ans
```

**Solution 2: (Heavy and Light Rows)**
```
Runtime: 1356 ms
Memory Usage: 16.6 MB
```
```python
class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        rows = [[c for c, val in enumerate(row) if val]
                for row in grid]
        N = sum(len(row) for row in grid)
        SQRTN = int(N**.5)

        ans = 0
        count = collections.Counter()
        for r, row in enumerate(rows):
            if len(row) >= SQRTN:
                target = set(row)
                for r2, row2 in enumerate(rows):
                    if r2 <= r and len(row2) >= SQRTN:
                        continue
                    found = sum(1 for c2 in row2 if c2 in target)
                    ans += found * (found - 1) // 2
            else:
                for pair in itertools.combinations(row, 2):
                    ans += count[pair]
                    count[pair] += 1

        return ans
```