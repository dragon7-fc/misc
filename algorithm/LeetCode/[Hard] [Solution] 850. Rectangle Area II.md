850. Rectangle Area II

We are given a list of (axis-aligned) `rectangles`.  Each `rectangle[i] = [x1, y1, x2, y2]` , where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the ith rectangle.

Find the total area covered by all `rectangles` in the plane.  Since the answer may be too large, **return it modulo 10^9 + 7**.

![850_rectangle_area_ii_pic.png](img/850_rectangle_area_ii_pic.png)
**Example 1:**
```
Input: [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: As illustrated in the picture.
```

**Example 2:**
```
Input: [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 10^18 modulo (10^9 + 7), which is (10^9)^2 = (-7)^2 = 49.
```

**Note:**

* 1 <= rectangles.length <= 200
* rectanges[i].length = 4
* 0 <= rectangles[i][j] <= 10^9
* The total area covered by all rectangles will never exceed 2^63 - 1 and thus will fit in a 64-bit signed integer.

# Solution
---
## Approach #1: Principle of Inclusion-Exclusion
**Intuition**

Say we have two rectangles, $A$ and $B$. The area of their union is:

$|A \cup B| = |A| + |B| - |A \cap B|$

Say we have three rectangles, $A, B, C$. The area of their union is:

$|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|$

This can be seen by drawing a Venn diagram.

Say we have four rectangles, $A, B, C, D$. The area of their union is:

$\begin{aligned} |A \cup B \cup C \cup D| =\,&\left( |A| + |B| + |C| + |D| \right) - \\ \,&\left(|A \cap B| + |A \cap C| + |A \cap D| + |B \cap C| + |B \cap D| + |C \cap D|\right) +\\ \,&\left(|A \cap B \cap C| + |A \cap B \cap D| + |A \cap C \cap D| + |B \cap C \cap D|\right) -\\ \,&\left(|A \cap B \cap C \cap D|\right) \end{aligned}$

In general, the area of the union of nn rectangles $A_1, A_2, \cdots , A_n$ will be:

$\bigg|\bigcup_{i=1}^n A_i\bigg| = \sum_{\emptyset \neq S \subseteq [n]} (-1)^{|S| + 1} \bigg| \bigcap_{i \in S} A_i$
 

**Algorithm**

If we do not know the above fact, we can prove it by considering any point in $\bigg|\bigcup_{i=1}^n A_i$. Say this point occurs in all $A_i (i \in S)$, and let $|S| = n$. Then on the right side, it is counted $\binom{n}{1} - \binom{n}{2} + \binom{n}{3} - \cdots \pm$ times. By considering the binomial expansion of $(1 - 1)^n$, this is in fact equal to $1$.

From Rectangle Area I, we know that the intersection of two axis-aligned rectangles is another axis-aligned rectangle (or nothing). So in particular, the intersection $\bigcap_{i \in S} A_i$ is always a rectangle (or nothing).

Now our algorithm proceeds as follows: for every subset $S$ of $\{1, 2, 3, \cdots, N\}$ (where $N$ is the number of rectangles), we'll calculate the intersection of the rectangles in that subset $\bigcap_{i \in S} A_i$, and then the area of that rectangle. This allows us to calculate algorithmically the right-hand side of the general equation we wrote earlier.

```python
class Solution(object):
    def rectangleArea(self, rectangles):
        def intersect(rec1, rec2):
            return [max(rec1[0], rec2[0]),
                    max(rec1[1], rec2[1]),
                    min(rec1[2], rec2[2]),
                    min(rec1[3], rec2[3])]

        def area(rec):
            dx = max(0, rec[2] - rec[0])
            dy = max(0, rec[3] - rec[1])
            return dx * dy

        ans = 0
        for size in xrange(1, len(rectangles) + 1):
            for group in itertools.combinations(rectangles, size):
                ans += (-1) ** (size + 1) * area(reduce(intersect, group))

        return ans % (10**9 + 7)
```

**Complexity Analysis**

* Time Complexity: $O(N * 2^N)$, where $N$ is the number of rectangles.

* Space Complexity: $O(N)$.

## Approach #2: Coordinate Compression
**Intuition**

![850_example.png](img/850_example.png)

Suppose instead of `rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]`, we had `[[0,0,200,200],[100,0,200,300],[100,0,300,100]]`. The answer would just be 100 times bigger.

What about if `rectangles = [[0,0,2,2],[1,0,2,3],[1,0,30002,1]]` ? Only the blue region would have area 30000 instead of 1.

Our idea is this: we'll take all the `x` and `y` coordinates, and re-map them to `0, 1, 2, ...` etc. For example, if `rectangles = [[0,0,200,200],[100,0,200,300],[100,0,300,100]]`, we could re-map it to `[[0,0,2,2],[1,0,2,3],[1,0,3,1]]`. Then, we can solve the problem with brute force. However, each region may actually represent some larger area, so we'll need to adjust for that at the end.

**Algorithm**

Re-map each `x` coordinate to `0, 1, 2, ....` Independently, re-map all `y` coordinates too.

We then have a problem that can be solved by brute force: for each rectangle with re-mapped coordinates `(rx1, ry1, rx2, ry2)`, we can fill the grid `grid[x][y] = True` for `rx1 <= x < rx2` and `ry1 <= y < ry2`.

Afterwards, each `grid[rx][ry]` represents the area `(imapx(rx+1) - imapx(rx)) * (imapy(ry+1) - imapy(ry))`, where if `x` got remapped to `rx`, then `imapx(rx) = x` ("inverse-map-x of remapped-x equals x"), and similarly for `imapy`.

```python
class Solution(object):
    def rectangleArea(self, rectangles):
        N = len(rectangles)
        Xvals, Yvals = set(), set()
        for x1, y1, x2, y2 in rectangles:
            Xvals.add(x1); Xvals.add(x2)
            Yvals.add(y1); Yvals.add(y2)

        imapx = sorted(Xvals)
        imapy = sorted(Yvals)
        mapx = {x: i for i, x in enumerate(imapx)}
        mapy = {y: i for i, y in enumerate(imapy)}

        grid = [[0] * len(imapy) for _ in imapx]
        for x1, y1, x2, y2 in rectangles:
            for x in xrange(mapx[x1], mapx[x2]):
                for y in xrange(mapy[y1], mapy[y2]):
                    grid[x][y] = 1

        ans = 0
        for x, row in enumerate(grid):
            for y, val in enumerate(row):
                if val:
                    ans += (imapx[x+1] - imapx[x]) * (imapy[y+1] - imapy[y])
        return ans % (10**9 + 7)
```

**Complexity Analysis**

* Time Complexity: $O(N^3)$, where $N$ is the number of rectangles.

* Space Complexity: $O(N^2)$.

## Approach #3: Line Sweep
**Intuition**

Imagine we pass a horizontal line from bottom to top over the shape. We have some active intervals on this horizontal line, which gets updated twice for each rectangle. In total, there are $2 * N$ events, and we can update our (up to $N$) active horizontal intervals for each update.

**Algorithm**

For a rectangle like `rec = [1,0,3,1]`, the first update is to add `[1, 3]` to the active set at `y = 0`, and the second update is to remove `[1, 3]` at `y = 1`. Note that adding and removing respects multiplicity - if we also added `[0, 2]` at `y = 0`, then removing `[1, 3]` at `y = 1` will still leave us with `[0, 2]` active.

This gives us a plan: create these two events for each rectangle, then process all the events in sorted order of `y`. The issue now is deciding how to process the events `add(x1, x2)` and `remove(x1, x2)` such that we are able to query() the total horizontal length of our active intervals.

We can use the fact that our `remove(...)` operation will always be on an interval that was previously added. Let's store all the `(x1, x2)` intervals in sorted order. Then, we can query() in linear time using a technique similar to a classic LeetCode problem, Merge Intervals.

```python
class Solution(object):
    def rectangleArea(self, rectangles):
        # Populate events
        OPEN, CLOSE = 0, 1
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, OPEN, x1, x2))
            events.append((y2, CLOSE, x1, x2))
        events.sort()

        def query():
            ans = 0
            cur = -1
            for x1, x2 in active:
                cur = max(cur, x1)
                ans += max(0, x2 - cur)
                cur = max(cur, x2)
            return ans

        active = []
        cur_y = events[0][0]
        ans = 0
        for y, typ, x1, x2 in events:
            # For all vertical ground covered, update answer
            ans += query() * (y - cur_y)

            # Update active intervals
            if typ is OPEN:
                active.append((x1, x2))
                active.sort()
            else:    
                active.remove((x1, x2))

            cur_y = y

        return ans % (10**9 + 7)
```

## Approach #4: Segment Tree
**Intuition and Algorithm**

As in Approach #3, we want to support `add(x1, x2)`, `remove(x1, x2)`, and `query()`. While outside the scope of a typical interview, this is the perfect setting for using a segment tree. For completeness, we include the following implementation.

You can learn more about Segment Trees by visiting the articles of these problems: Falling Squares, Number of Longest Increasing Subsequence.

```python
class Node(object):
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.total = self.count = 0
        self._left = self._right = None

    @property
    def mid(self):
        return (self.start + self.end) / 2

    @property
    def left(self):
        self._left = self._left or Node(self.start, self.mid)
        return self._left

    @property
    def right(self):
        self._right = self._right or Node(self.mid, self.end)
        return self._right

    def update(self, i, j, val):
        if i >= j: return 0
        if self.start == i and self.end == j:
            self.count += val
        else:
            self.left.update(i, min(self.mid, j), val)
            self.right.update(max(self.mid, i), j, val)

        if self.count > 0:
            self.total = X[self.end] - X[self.start]
        else:
            self.total = self.left.total + self.right.total

        return self.total

class Solution(object):
    def rectangleArea(self, rectangles):
        OPEN, CLOSE = 1, -1
        events = []
        global X
        X = set()
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, OPEN, x1, x2))
            events.append((y2, CLOSE, x1, x2))
            X.add(x1)
            X.add(x2)
        events.sort()

        X = sorted(X)
        Xi = {x: i for i, x in enumerate(X)}

        active = Node(0, len(X) - 1)
        ans = 0
        cur_x_sum = 0
        cur_y = events[0][0]

        for y, typ, x1, x2 in events:
            ans += cur_x_sum * (y - cur_y)
            cur_x_sum = active.update(Xi[x1], Xi[x2], typ)
            cur_y = y

        return ans % (10**9 + 7)
```

**Complexity Analysis**

* Time Complexity: $O(N \log N)$, where $N$ is the number of rectangles.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution 1:**