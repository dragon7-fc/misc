757. Set Intersection Size At Least Two

An integer interval `[a, b]` (for integers `a < b`) is a set of all consecutive integers from `a` to `b`, including `a` and `b`.

Find the minimum size of a set S such that for every integer interval A in `intervals`, the intersection of S with A has size at least 2.

**Example 1:**
```
Input: intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]
Output: 3
Explanation:
Consider the set S = {2, 3, 4}.  For each interval, there are at least 2 elements from S in the interval.
Also, there isn't a smaller size set that fulfills the above condition.
Thus, we output the size of this set, which is 3.
```

**Example 2:**
```
Input: intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
Output: 5
Explanation:
An example of a minimum sized set is {1, 2, 3, 4, 5}.
```

**Note:**

* `intervals` will have length in range `[1, 3000]`.
* `intervals[i]` will have length `2`, representing some integer interval.
* `intervals[i][j]` will be an integer in `[0, 10^8]`.

# Solution
---
## Approach #1: Greedy [Accepted]
**Intuition**

Let's try to solve a simpler problem: what is the answer when the set intersection size is at least one?

Sort the points. Take the last interval `[s, e]`, which point on this interval will be in `S`? Since every other interval has start point `<= s`, it is strictly better to choose `s` as the start. So we can repeatedly take `s` in our set `S` and remove all intervals containing `s`.

We will try to extend this solution to the case when we want an intersection of size two.

**Algorithm**

For each interval, we will perform the algorithm described above, storing a `todo` multiplicity which starts at `2`. As we identify points in `S`, we will subtract from these multiplicities as appropriate.

One case that is important to handle is the following: `[[1, 2], [2, 3], [2, 4], [4, 5]]`. If we put `4, 5` in `S`, then we put `2` in `S`, when handling `[2, 3]` we need to put `3` in `S`, not `2` which was already put.

We can handle this case succinctly by sorting intervals `[s, e]` by `s` ascending, then `e` descending. This makes it so that any interval encountered with the same `s` has the lowest possible `e`, and so it has the highest multiplicity. When at interval `[s, e]` and choosing points to be included into `S`, it will always be the case that the start of the interval (either `s` or `s`, `s+1`) will be unused.

```python
class Solution(object):
    def intersectionSizeTwo(self, intervals):
        intervals.sort(key = lambda (s, e): (s, -e))
        todo = [2] * len(intervals)
        ans = 0
        while intervals:
            (s, e), t = intervals.pop(), todo.pop()
            for p in xrange(s, s+t):
                for i, (s0, e0) in enumerate(intervals):
                    if todo[i] and p <= e0:
                        todo[i] -= 1
                ans += 1
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the length of intervals.

* Space Complexity: $O(N)$.

# Solution
---
**Solution 1: (Greedy)**
```
Runtime: 1776 ms
Memory Usage: 14.9 MB
```
```python
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))
        todo = [2] * len(intervals)
        ans = 0
        while intervals:
            (s, e), t = intervals.pop(), todo.pop()
            for p in range(s, s+t):
                for i, (s0, e0) in enumerate(intervals):
                    if todo[i] and p <= e0:
                        todo[i] -= 1
                ans += 1
        return ans
```

**Solution 2: (Greedy)**
```
Runtime: 180 ms
Memory Usage: 17.7 MB
```
```c++
class Solution {
public:
    int intersectionSizeTwo(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](vector<int>&a, vector<int>&b) {
            if(a[1] != b[1]) {
                return a[1] < b[1];
            } else {
                return a[0] > b[0];
            }
        });
        
        int ans = 0;
        int pre_left = -1, pre_right = -1;
        for(int i = 0; i < intervals.size(); i++) {
            if(intervals[i][0] <= pre_left) continue;
            
            if(intervals[i][0] > pre_right) {
                ans += 2;
                pre_right = intervals[i][1];
                pre_left = pre_right - 1;
            } else {
                ans += 1;
                pre_left = pre_right;
                pre_right = intervals[i][1];
            }
        }
        
        return ans;
    }
};
```

**Solution 3: (Greedy)**

Sort intervals by end. The right-most 2 points are the one we are interested in. When a new interval comes, reuse the current right-most 2 points as much as possible. If can't reuse, then introduce new points to the right-most side of new interval.

```
Runtime: 300 ms
Memory Usage: 15.4 MB
```
```python
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1]) # sort by end-point
        ans = 0
        pre = []
        for (s, t) in intervals:
            if not pre or pre[1] < s:
                ans += 2
                pre = [t-1, t]
            elif pre[0] < s:
                pre = [pre[1], t]
                ans += 1
        return ans
```

**Solution 4: (Sort, Greedy, sort by smallest end then largest start, only care about right most 2 point)**

      v v
              v v
                v v
    1 2 3 4 5 6 7 8, ans = 5
    xxxxx
            xxxxx
        xxxxxxxxx
                xxx

```
Runtime: 4 ms, Beats 65.43%
Memory: 21.66 MB, Beats 90.12%
```
```c++
class Solution {
public:
    int intersectionSizeTwo(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](auto &ia, auto &ib){
            if (ia[1] != ib[1]) {
                return ia[1] < ib[1];
            }
            return ia[0] > ib[0];
        });
        int n = intervals.size(), i, pst = intervals[0][1] - 1, ped = intervals[0][1], st, ed, ans = 2;
        for (i = 1; i < n; i ++) {
            st = intervals[i][0];
            ed = intervals[i][1];
            if (ped < st) {
                pst = ed - 1;
                ped = ed;
                ans += 2;
            } else if (pst < st) {
                pst = ped;
                ped = ed;
                ans += 1;
            }
        }
        return ans;
    }
};
```
