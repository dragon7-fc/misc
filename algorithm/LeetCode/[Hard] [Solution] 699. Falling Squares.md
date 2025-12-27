699. Falling Squares

On an infinite number line (x-axis), we drop given squares in the order they are given.

The i-th square dropped `(positions[i] = (left, side_length))` is a square with the left-most point being `positions[i][0]` and sidelength `positions[i][1]`.

The square is dropped with the bottom edge parallel to the number line, and from a higher height than all currently landed squares. We wait for each square to stick before dropping the next.

The squares are infinitely sticky on their bottom edge, and will remain fixed to any positive length surface they touch (either the number line or another square). Squares dropped adjacent to each other will not stick together prematurely.

 
Return a list `ans` of heights. Each height `ans[i]` represents the current highest height of any square we have dropped, after dropping squares represented by `positions[0], positions[1], ..., positions[i]`.

**Example 1:**
```
Input: [[1, 2], [2, 3], [6, 1]]
Output: [2, 5, 5]
Explanation:
After the first drop of positions[0] = [1, 2]: _aa _aa ------- The maximum height of any square is 2.

After the second drop of positions[1] = [2, 3]: __aaa __aaa __aaa _aa__ _aa__ -------------- The maximum height of any square is 5. The larger square stays on top of the smaller square despite where its center of gravity is, because squares are infinitely sticky on their bottom edge.

After the third drop of positions[1] = [6, 1]: __aaa __aaa __aaa _aa _aa___a -------------- The maximum height of any square is still 5. Thus, we return an answer of [2, 5, 5].
```
 

 
**Example 2:**
```
Input: [[100, 100], [200, 100]]
Output: [100, 100]
Explanation: Adjacent squares don't get stuck prematurely - only their bottom edge can stick to surfaces.
``` 

**Note:**

* `1 <= positions.length <= 1000`.
* `1 <= positions[i][0] <= 10^8`.
* `1 <= positions[i][1] <= 10^6`.


# Solution
---
## Approach Framework
**Intuition**

Intuitively, there are two operations: `update`, which updates our notion of the board (number line) after dropping a square; and `query`, which finds the largest height in the current board on some interval. We will work on implementing these operations.

**Coordinate Compression**

In the below approaches, since there are only up to `2 * len(positions)` critical points, namely the left and right edges of each square, we can use a technique called coordinate compression to map these critical points to adjacent integers, as shown in the code snippets below.

For brevity, these snippets are omitted from the remaining solutions.

```python
coords = set()
for left, size in positions:
    coords.add(left)
    coords.add(left + size - 1)
index = {x: i for i, x in enumerate(sorted(coords))}
```

## Approach 1: Offline Propagation
**Intuition**

Instead of asking the question "what squares affect this query?", lets ask the question "what queries are affected by this square?"

**Algorithm**

Let `qans[i]` be the maximum height of the interval specified by `positions[i]`. At the end, we'll return a running max of `qans`.

For each square `positions[i]`, the maximum height will get higher by the size of the square we drop. Then, for any future squares that intersect the interval `[left, right)` (where `left = positions[i][0], right = positions[i][0] + positions[i][1]`), we'll update the maximum height of that interval.

```python
class Solution(object):
    def fallingSquares(self, positions):
        qans = [0] * len(positions)
        for i, (left, size) in enumerate(positions):
            right = left + size
            qans[i] += size
            for j in xrange(i+1, len(positions)):
                left2, size2 = positions[j]
                right2 = left2 + size2
                if left2 < right and left < right2: #intersect
                    qans[j] = max(qans[j], qans[i])

        ans = []
        for x in qans:
            ans.append(max(ans[-1], x) if ans else x)
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the length of positions. We use two for-loops, each of complexity $O(N)$.

* Space Complexity: $O(N)$, the space used by qans and ans.

## Approach 2: Brute Force with Coordinate Compression
**Intuition and Algorithm**

Let `N = len(positions)`. After mapping the board to a board of length at most $2* N \leq 2000$, we can brute force the answer by simulating each square's drop directly.

Our answer is either the current answer or the height of the square that was just dropped, and we'll update it appropriately.

```python
class Solution(object):
    def fallingSquares(self, positions):
        #Coordinate Compression
        #index = ...

        heights = [0] * len(index)
        def query(L, R):
            return max(heights[i] for i in xrange(L, R+1))

        def update(L, R, h):
            for i in xrange(L, R+1):
                heights[i] = max(heights[i], h)

        best = 0
        ans = []
        for left, size in positions:
            L = index[left]
            R = index[left + size - 1]
            h = query(L, R) + size
            update(L, R, h)
            best = max(best, h)
            ans.append(best)

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the length of positions. We use two for-loops, each of complexity $O(N)$ (because of coordinate compression.)

* Space Complexity: $O(N)$, the space used by heights.

## Approach 3: Block (Square Root) Decomposition
**Intuition**

Whenever we perform operations (like `update` and `query`) on some interval in a domain, we could segment that domain with size $W$ into blocks of size $\sqrt{W}$.

Then, instead of a typical brute force where we update our array `heights` representing the board, we will also hold another array `blocks`, where `blocks[i]` represents the $B = \lfloor \sqrt{W} \rfloor$ elements `heights[B*i], heights[B*i + 1], ..., heights[B*i + B-1]`. This allows us to write to the array in $O(B)$ operations.

**Algorithm**

Let's get into the details. We actually need another array, `blocks_read`. When we update some element `i` in block `b = i / B`, we'll also update `blocks_read[b]`. If later we want to read the entire block, we can read from here (and stuff written to the whole block in `blocks[b]`.)

When we write to a block, we'll write in `blocks[b]`. Later, when we want to read from an element `i` in block `b = i / B`, we'll read from `heights[i]` and `blocks[b]`.

Our process for managing `query` and `update` will be similar. While left isn't a multiple of `B`, we'll proceed with a brute-force-like approach, and similarly for right. At the end, `[left, right+1)` will represent a series of contiguous blocks: the interval will have length which is a multiple of `B`, and left will also be a multiple of `B`.

```python
class Solution(object):
    def fallingSquares(self, positions):
        #Coordinate compression
        #index = ...

        W = len(index)
        B = int(W**.5)
        heights = [0] * W
        blocks = [0] * (B+2)
        blocks_read = [0] * (B+2)

        def query(left, right):
            ans = 0
            while left % B and left <= right:
                ans = max(ans, heights[left], blocks[left / B])
                left += 1
            while right % B != B-1 and left <= right:
                ans = max(ans, heights[right], blocks[right / B])
                right -= 1
            while left <= right:
                ans = max(ans, blocks[left / B], blocks_read[left / B])
                left += B
            return ans

        def update(left, right, h):
            while left % B and left <= right:
                heights[left] = max(heights[left], h)
                blocks_read[left / B] = max(blocks_read[left / B], h)
                left += 1
            while right % B != B-1 and left <= right:
                heights[right] = max(heights[right], h)
                blocks_read[right / B] = max(blocks_read[right / B], h)
                right -= 1
            while left <= right:
                blocks[left / B] = max(blocks[left / B], h)
                left += B

        best = 0
        ans = []
        for left, size in positions:
            L = index[left]
            R = index[left + size - 1]
            h = query(L, R) + size
            update(L, R, h)
            best = max(best, h)
            ans.append(best)

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N\sqrt{N})$, where $N$ is the length of positions. Each query and update has complexity $O(\sqrt{N})$.

* Space Complexity: $O(N)$, the space used by heights.

## Approach 4: Segment Tree with Lazy Propagation
**Intuition**

If we were familiar with the idea of a segment tree (which supports queries and updates on intervals), we can immediately crack the problem.

**Algorithm**

Segment trees work by breaking intervals into a disjoint sum of component intervals, whose number is at most `log(width)`. The motivation is that when we change an element, we only need to change `log(width)` many intervals that aggregate on an interval containing that element.

When we want to update an interval all at once, we need to use lazy propagation to ensure good run-time complexity. This topic is covered in more depth here.

With such an implementation in hand, the problem falls out immediately.

```python
class SegmentTree(object):
    def __init__(self, N, update_fn, query_fn):
        self.N = N
        self.H = 1
        while 1 << self.H < N:
            self.H += 1

        self.update_fn = update_fn
        self.query_fn = query_fn
        self.tree = [0] * (2 * N)
        self.lazy = [0] * N

    def _apply(self, x, val):
        self.tree[x] = self.update_fn(self.tree[x], val)
        if x < self.N:
            self.lazy[x] = self.update_fn(self.lazy[x], val)

    def _pull(self, x):
        while x > 1:
            x /= 2
            self.tree[x] = self.query_fn(self.tree[x*2], self.tree[x*2 + 1])
            self.tree[x] = self.update_fn(self.tree[x], self.lazy[x])

    def _push(self, x):
        for h in xrange(self.H, 0, -1):
            y = x >> h
            if self.lazy[y]:
                self._apply(y * 2, self.lazy[y])
                self._apply(y * 2+ 1, self.lazy[y])
                self.lazy[y] = 0

    def update(self, L, R, h):
        L += self.N
        R += self.N
        L0, R0 = L, R
        while L <= R:
            if L & 1:
                self._apply(L, h)
                L += 1
            if R & 1 == 0:
                self._apply(R, h)
                R -= 1
            L /= 2; R /= 2
        self._pull(L0)
        self._pull(R0)

    def query(self, L, R):
        L += self.N
        R += self.N
        self._push(L); self._push(R)
        ans = 0
        while L <= R:
            if L & 1:
                ans = self.query_fn(ans, self.tree[L])
                L += 1
            if R & 1 == 0:
                ans = self.query_fn(ans, self.tree[R])
                R -= 1
            L /= 2; R /= 2
        return ans

class Solution(object):
    def fallingSquares(self, positions):
        #Coordinate compression
        #index = ...

        tree = SegmentTree(len(index), max, max)
        best = 0
        ans = []
        for left, size in positions:
            L, R = index[left], index[left + size - 1]
            h = tree.query(L, R) + size
            tree.update(L, R, h)
            best = max(best, h)
            ans.append(best)

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N \log N)$, where $N$ is the length of positions. This is the run-time complexity of using a segment tree.

* Space Complexity: $O(N)$, the space used by our tree.

# Submissions
---
**Solution 1: (Offline Propagation)**
```
Runtime: 668 ms
Memory Usage: 13.1 MB
```
```python
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        qans = [0] * len(positions)
        for i, (left, size) in enumerate(positions):
            right = left + size
            qans[i] += size
            for j in range(i+1, len(positions)):
                left2, size2 = positions[j]
                right2 = left2 + size2
                if left2 < right and left < right2: #intersect
                    qans[j] = max(qans[j], qans[i])

        ans = []
        for x in qans:
            ans.append(max(ans[-1], x) if ans else x)
        return ans
```

**Solution 2: (Brute Force with Coordinate Compression)**
```
Runtime: 164 ms
Memory Usage: 13.4 MB
```
```python
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        #Coordinate Compression
        coords = set()
        for left, size in positions:
            coords.add(left)
            coords.add(left + size - 1)
        index = {x: i for i, x in enumerate(sorted(coords))}

        heights = [0] * len(index)
        def query(L, R):
            return max(heights[i] for i in range(L, R+1))

        def update(L, R, h):
            for i in range(L, R+1):
                heights[i] = max(heights[i], h)

        best = 0
        ans = []
        for left, size in positions:
            L = index[left]
            R = index[left + size - 1]
            h = query(L, R) + size
            update(L, R, h)
            best = max(best, h)
            ans.append(best)

        return ans
```

**Solution 3: (Block (Square Root) Decomposition)**
```
Runtime: 284 ms
Memory Usage: 13.4 MB
```
```python
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        #Coordinate Compression
        coords = set()
        for left, size in positions:
            coords.add(left)
            coords.add(left + size - 1)
        index = {x: i for i, x in enumerate(sorted(coords))}

        W = len(index)
        B = int(W**.5)
        heights = [0] * W
        blocks = [0] * (B+2)
        blocks_read = [0] * (B+2)

        def query(left, right):
            ans = 0
            while left % B and left <= right:
                ans = max(ans, heights[left], blocks[left // B])
                left += 1
            while right % B != B-1 and left <= right:
                ans = max(ans, heights[right], blocks[right // B])
                right -= 1
            while left <= right:
                ans = max(ans, blocks[left // B], blocks_read[left // B])
                left += B
            return ans

        def update(left, right, h):
            while left % B and left <= right:
                heights[left] = max(heights[left], h)
                blocks_read[left // B] = max(blocks_read[left // B], h)
                left += 1
            while right % B != B-1 and left <= right:
                heights[right] = max(heights[right], h)
                blocks_read[right // B] = max(blocks_read[right // B], h)
                right -= 1
            while left <= right:
                blocks[left // B] = max(blocks[left // B], h)
                left += B

        best = 0
        ans = []
        for left, size in positions:
            L = index[left]
            R = index[left + size - 1]
            h = query(L, R) + size
            update(L, R, h)
            best = max(best, h)
            ans.append(best)

        return ans
```

**Solution 4: (Segment Tree with Lazy Propagation)**
```
Runtime: 368 ms
Memory Usage: 13.5 MB
```
```python
class SegmentTree(object):
    def __init__(self, N, update_fn, query_fn):
        self.N = N
        self.H = 1
        while 1 << self.H < N:
            self.H += 1

        self.update_fn = update_fn
        self.query_fn = query_fn
        self.tree = [0] * (2 * N)
        self.lazy = [0] * N

    def _apply(self, x, val):
        self.tree[x] = self.update_fn(self.tree[x], val)
        if x < self.N:
            self.lazy[x] = self.update_fn(self.lazy[x], val)

    def _pull(self, x):
        while x > 1:
            x //= 2
            self.tree[x] = self.query_fn(self.tree[x*2], self.tree[x*2 + 1])
            self.tree[x] = self.update_fn(self.tree[x], self.lazy[x])

    def _push(self, x):
        for h in range(self.H, 0, -1):
            y = x >> h
            if self.lazy[y]:
                self._apply(y * 2, self.lazy[y])
                self._apply(y * 2+ 1, self.lazy[y])
                self.lazy[y] = 0

    def update(self, L, R, h):
        L += self.N
        R += self.N
        L0, R0 = L, R
        while L <= R:
            if L & 1:
                self._apply(L, h)
                L += 1
            if R & 1 == 0:
                self._apply(R, h)
                R -= 1
            L //= 2; R //= 2
        self._pull(L0)
        self._pull(R0)

    def query(self, L, R):
        L += self.N
        R += self.N
        self._push(L); self._push(R)
        ans = 0
        while L <= R:
            if L & 1:
                ans = self.query_fn(ans, self.tree[L])
                L += 1
            if R & 1 == 0:
                ans = self.query_fn(ans, self.tree[R])
                R -= 1
            L //= 2; R //= 2
        return ans

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        #Coordinate Compression
        coords = set()
        for left, size in positions:
            coords.add(left)
            coords.add(left + size - 1)
        index = {x: i for i, x in enumerate(sorted(coords))}

        tree = SegmentTree(len(index), max, max)
        best = 0
        ans = []
        for left, size in positions:
            L, R = index[left], index[left + size - 1]
            h = tree.query(L, R) + size
            tree.update(L, R, h)
            best = max(best, h)
            ans.append(best)

        return ans
```

**Solution 5: (Segment Tree with Lazy Propagation, range max)**

6  |      _______
5  |     |       |
4  |     |   2   |
3  |   __|__ ____|
2  |  |     |         __
1  |  |  1  |        |3 |
---x-----------------------------
   0  1  2  3  4  5  6  7  8  9

                   0 (5)
              /         \
            1 (5)         2 (1)
          /    \        /    \
        3 (5)   4 (5)  5 (1)  6
      /   \         
     7 (2) 8 (5)        
x    1     2    4      6

st   1   2   4   6
mp
1:  0
2:  1
4:  2
6:  3

============================================
u0:   
    0  1  2  3  4  5  6  7  8
    ul ur
------------------------------
    p
    l           r
------------------------------
       p
    l     r
------------------------------
             p
    l  r
------------------------------
                         p
    lrx
------------------------------
       lrx

     0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
dp   2  2     2                                                            
Lazy                      2  2

============================================
q1:
    0  1  2  3  4  5  6  7  8  9  10
       ql qr
----------------------------------
    p
    l           r
----------------------------------
       p
    l     r
-----------------------------------
             p
    l  r
-----------------------------------
                         p
    lr
-----------------------------------
       lrx                  p
-----------------------------------
                p
          lrx

     0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
dp   2  2     2           2  2                                             
Lazy                          

============================================
u1:
    0  1  2  3  4  5  6  7  8  9  10
       ul ur
----------------------------------------
    p
    l          r
-----------------------------------------
       p
    l     r
-----------------------------------------
             p
    l  r
-----------------------------------------
                         p
    lr
-----------------------------------------
                            p
       lrx
-----------------------------------
                p
          lrx
    

     0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
dp   5  5     5  5        2  5                                             
Lazy                          

============================================
q2:
     0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
dp   5  5     5  5        2  5                                             
Lazy                          

============================================
u2:
    0  1  2  3  4  5  6  7  8  9  10
             ulr
--------------------------------------
    p
    l           r
--------------------------------------
       p
    l     r
--------------------------------------
             p
    l  r
---------------------------------------
                          p
    lr
---------------------------------------
                             p
       lr
---------------------------------------
                p
          lr
----------------------------------------
          p
             l  r
----------------------------------------
                   p
             lrx

     0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
dp   5  5  1  5  5  1     2  5                                             
Lazy                          

```
Runtime: 16  ms, Beats 41.50%
Memory: 18.96 MB, Beats 33.72%
```
```c++
class SegmentTree{
    vector<int> dp, lazy;
public:
    SegmentTree(int n) { 
        dp.resize(4 * n);
        lazy.resize(4 * n);
    }
    void update(int ti, int left, int right, int u_left, int u_right, int val) {
        if (lazy[ti] != 0) {
            dp[ti] = max(dp[ti], lazy[ti]);
            if (left != right){
                lazy[2 * ti + 1] = max(lazy[2 * ti + 1], dp[ti]);
                lazy[2 * ti + 2] = max(lazy[2 * ti + 2], dp[ti]);
            }
            lazy[ti] = 0;
        }
        if (u_left > right || u_right < left) {
            return;
        }
        if (u_left <= left && right <= u_right) {
            dp[ti] = val;
            if (left != right) {
                lazy[2 * ti + 1] = max(lazy[2 * ti + 1], dp[ti]);
                lazy[2 * ti + 2] = max(lazy[2 * ti + 2], dp[ti]);
            }
            return;
        }
        int mid = left + (right - left) / 2;
        update(2 * ti + 1, left, mid, u_left, u_right, val);
        update(2 * ti + 2, mid + 1, right, u_left, u_right, val);
        dp[ti] = max(dp[2 * ti + 1], dp[2 * ti + 2]);
    }
    int query(int ti, int left, int right, int& q_left, int& q_right) {
        if (lazy[ti] != 0) {
            dp[ti] = max(dp[ti], lazy[ti]);
            if (left != right) {
                lazy[2 * ti + 1] = max(lazy[2 * ti + 1], dp[ti]);
                lazy[2 * ti + 2] = max(lazy[2 * ti + 2], dp[ti]);
            }
            lazy[ti] = 0;
        }
        if (q_left > right || q_right < left) {
            return 0;
        }
        if (q_left <= left && right <= q_right) {
            return dp[ti];
        }
        int mid = left + (right - left) / 2;
        return max(query(2 * ti + 1, left, mid, q_left, q_right),
                    query(2 * ti + 2, mid + 1, right, q_left, q_right));
    }
};

class Solution {
public:
    vector<int> fallingSquares(vector<vector<int>>& positions) {
        set<int> st;
        for (auto &pos : positions) {
            st.insert(pos[0]);
            st.insert(pos[0] + pos[1] - 1);
        }
        unordered_map<int, int> mp;
        int i = 0, n, left, right, cur;
        for (auto x : st){
            mp[x] = i;
            i += 1;
        }
        n = i;
        SegmentTree sgt(n);
        int mx = 0;
        vector<int> ans;
        for (auto &pos : positions) {
            left = mp[pos[0]];
            right = mp[pos[0] + pos[1] - 1];
            cur = sgt.query(0, 0, n, left, right);
            cur += pos[1];
            sgt.update(0, 0, n, left, right, cur);
            mx = max(mx, cur);
            ans.push_back(mx);
        }
        return ans;
    }
};
```
