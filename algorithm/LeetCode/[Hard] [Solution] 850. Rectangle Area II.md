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

**Complexity Analysis**

* Time Complexity: $O(N^2 \log N)$, where $N$ is the number of rectangles.

* Space Complexity: $O(N)$.

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
**Solution 1: (Coordinate Compression)**
```
Runtime: 136 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
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
            for x in range(mapx[x1], mapx[x2]):
                for y in range(mapy[y1], mapy[y2]):
                    grid[x][y] = 1

        ans = 0
        for x, row in enumerate(grid):
            for y, val in enumerate(row):
                if val:
                    ans += (imapx[x+1] - imapx[x]) * (imapy[y+1] - imapy[y])
        return ans % (10**9 + 7)
```

**Solution 2: (Line Sweep)**
```
Runtime: 48 ms
Memory Usage: 13 MB
```
```python
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
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

**Solution 3: (Segment Tree)**
```
Runtime: 84 ms
Memory Usage: 12.6 MB
```
```python
class Node(object):
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.total = self.count = 0
        self._left = self._right = None

    @property
    def mid(self):
        return (self.start + self.end) // 2

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

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
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

**Solution 4: (Coordinate Compression, coordinate transformation)**

           0             1                           2
    [0,0,100,100] [10000,10000,20000, 20000] [50,50,150,150]

 2000                   -----x
                        | 1  |
 1000                   x-----
  150     --------x
  100 ----|---x 2 |
   50 | 0 x---|----
    0 x--------
      0  50  100 150  1000  2000
  
   dpy
5 2000
4 1000                   x
3  150
2  100      x  x
1   50  x   x  x
0    0  x   x
        0  50 100 150  1000 2000 dpx
        0  1    2    3    4    5

```
Runtime: 18 ms, Beats 19.11%
Memory: 15.08 MB, Beats 18.85%
```
```c++
class Solution {
public:
    int rectangleArea(vector<vector<int>>& rectangles) {
        int MOD = 1e9 + 7;
        set<int> stx, sty;
        for (auto r: rectangles) {
            stx.insert(r[0]);
            stx.insert(r[2]);
            sty.insert(r[1]);
            sty.insert(r[3]);
        }
        vector<long long> dpx(stx.begin(), stx.end());
        vector<long long> dpy(sty.begin(), sty.end());
        unordered_map<long long,int> mx, my;
        int i, j, m = dpx.size(), n = dpy.size();
        for (i = 0; i < m; i ++) {
            mx[dpx[i]] = i;
        }
        for (j = 0; j < n; j ++) {
            my[dpy[j]] = j;
        }
        vector<vector<int>> g(m, vector<int>(n));
        for (auto r: rectangles) {
            for (i = mx[r[0]]; i < mx[r[2]]; i ++) {
                for (j = my[r[1]]; j < my[r[3]]; j ++) {
                    g[i][j] = 1;
                }
            }
        }
        long long ans = 0;
        for (i = 0; i < m-1; i ++) {
            for (j = 0; j < n-1; j ++) {
                if (g[i][j]) {
                    ans += (dpx[i+1] - dpx[i]) * (dpy[j+1] - dpy[j]);
                    ans %= MOD;
                }
            }
        }
        return ans;
    }
};
```

**Solution 5: (Line Sweep, open close event)**

 2000                   -----x
                        | 1  |
 1000                   x-----
  150     --------x                <dy
  100 ----|---x 2 |                |
   50 | 0 x---|----                
    0 x--------                   
      0  50  100 150  1000  2000
      ^e0 ^e1 ^e2 ^e3   ^e4   ^e5
              ^px ^x
w         e0  e0  e0        e4
              e1

```
Runtime: 3 ms, Beats 64.06%
Memory: 12.36 MB, Beats 65.10%
```
```c++
class Solution {
public:
    int rectangleArea(vector<vector<int>>& rectangles) {
        int n = rectangles.size(), i, MOD = 1e9 + 7, px, cur;
        long long dy, ans = 0;
        vector<tuple<int,int,int,int,int>> dp;
        for (i = 0; i < n; i ++) {
            dp.push_back({rectangles[i][0], 0, rectangles[i][1], rectangles[i][3], i});
            dp.push_back({rectangles[i][2], 1, rectangles[i][1], rectangles[i][3], i});
        }
        sort(dp.begin(), dp.end());
        vector<pair<int,int>> w;
        px = get<0>(dp[0]);
        for (auto [x, t, y1, y2, i]: dp) {
            dy = 0;
            cur = -1;
            for (auto [cy1, cy2]: w) {
                cur = max(cur, cy1);
                dy += max(0, cy2 - cur);
                cur = max(cur, cy2);
            }
            ans += dy * (x - px);
            ans %= MOD;
            if (t == 0) {
                w.push_back({y1, y2});
                sort(w.begin(), w.end());
            } else {
                auto it = find(w.begin(), w.end(), make_pair(y1, y2));
                w.erase(it);
            }
            px = x;
        }
        return ans;
    }
};
```

**Solution 6: (Segment Tree)**

    rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]

       3      |--x data[5]
       2   ------x data[4]
       1   |  |--|--x data[3]
       0   x--x-----|
           0  1  2  3
                      
data                    y  t
> 0        x     x      0  1
  1           x  x      0  1
  2           x     x   0  1
  3           x     x   1 -1
  4        x     x      2 -1
  5           x  x      3 -1

dp  {0, 1 ,2 ,3}
        root  ->   [0, 1, 2, 3] 0 2
                   /           \
            [0, 1] 1 1          [1, 2, 3] 0 1
                                /       \
                            [1, 2] 1 1  [2, 3] 0 0

```
Runtime: 3 ms, Beats 63.78%
Memory: 14.63 MB, Beats 20.73%
```
```c++
const int MOD = 1e9+7;
struct Node {
    int start; //start coordinate of a range
    int end; // end coordinate of a range
    int cnt; // count how many times this range has been covered by rectangles
    int area; // area that is covered within this range
    Node *left; //left sub-segement tree
    Node *right;// right sub-segment tree
    Node (int s, int e, int cn, int ar, Node *l_node, Node *r_node) {
        start = s;
        end = e;
        cnt = cn;
        area = ar;
        left = l_node;
        right = r_node;
    }
};

static bool cmp(const vector<int>&a, const vector<int> &b) {
    if (a[2] != b[2])
        return a[2] < b[2];
    return a[0] < b[0];
}

Node* build(const vector<int> &nums, int s, int e){        
    if (s >= e)
        return NULL;
    if (e - s == 1) {
        return new Node(nums[s], nums[s+1], 0, 0, NULL, NULL);
    }   
    int mid = (s + e)/2;
    Node *left = build(nums, s, mid);
    Node *right = build(nums, mid, e);
    return new Node(left->start, right->end, 0, 0, left, right);
}

void update(Node *node, int s, int e, const int t){
    if (!node) {
        return;
    }
    if (s >= node->end || e <= node->start) {
        return;
    }
    if (s <= node->start && e >= node->end) {
        node->cnt += t;
    } else {
        update(node->left, s, e, t); //update left tree
        update(node->right, s, e, t); //update right tree
    }
    if (node->cnt) {
        node->area = node->end - node->start;
    } else {
        if (node->left && node->right) {
            node->area = node->left->area + node->right->area;
        } else {
            node->area = 0;
        }
    }
}

class Solution {
public:
    int rectangleArea(vector<vector<int>>& rectangles) {
        const int m = rectangles.size();
        if (m == 0) {
            return 0;
        }
        set<int> x_st;
        for (const vector<int> &v : rectangles) {
            x_st.insert(v[0]);
            x_st.insert(v[2]);
        }               
        vector<int> dp(x_st.begin(), x_st.end());
        long long ans = 0;
        Node *root = build(dp, 0, dp.size()-1);        
        
        vector<vector<int>> data;
        vector<int> cur(4);
        for (const vector<int> &v: rectangles){
            cur[0] = v[0];  // x_left
            cur[1] = v[2];  // x_right
            cur[2] = v[1];  // y_left
            cur[3] = 1;
            data.push_back(cur);
            cur[2] = v[3];  // y_right
            cur[3] = -1;
            data.push_back(cur);            
        }
        
        sort(data.begin(), data.end(), cmp);
        
        update(root, data[0][0], data[0][1], data[0][3]);
        for (int i = 1; i < data.size(); i++){
            long long h = data[i][2] - data[i-1][2];        
            long long w = root->area;            
            if (h > 0) {
                ans += (w*h) % MOD;
                ans %= MOD;
            }
            update(root, data[i][0], data[i][1], data[i][3]);       
        }
        return ans;
    }
};
```
