939. Minimum Area Rectangle

Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return `0`.

 

**Example 1:**
```
Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
```

**Example 2:**
```
Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
```

**Note:**

* `1 <= points.length <= 500`
* `0 <= points[i][0] <= 40000`
* `0 <= points[i][1] <= 40000`
* All points are distinct.

# Solution
---
## Approach 1: Sort by Column
**Intuition**

Count each rectangle by right-most edge.

**Algorithm**

Group the points by `x` coordinates, so that we have columns of points. Then, for every pair of points in a column (with coordinates `(x,y1)` and `(x,y2)`), check for the smallest rectangle with this pair of points as the rightmost edge. We can do this by keeping memory of what pairs of points we've seen before.

```python
class Solution(object):
    def minAreaRect(self, points):
        columns = collections.defaultdict(list)
        for x, y in points:
            columns[x].append(y)
        lastx = {}
        ans = float('inf')

        for x in sorted(columns):
            column = columns[x]
            column.sort()
            for j, y2 in enumerate(column):
                for i in xrange(j):
                    y1 = column[i]
                    if (y1, y2) in lastx:
                        ans = min(ans, (x - lastx[y1,y2]) * (y2 - y1))
                    lastx[y1, y2] = x
        return ans if ans < float('inf') else 0
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the length of points.

* Space Complexity: $O(N)$.

## Approach 2: Count by Diagonal
**Intuition**

For each pair of points in the array, consider them to be the long diagonal of a potential rectangle. We can check if all 4 points are there using a Set.

For example, if the points are `(1, 1)` and `(5, 5)`, we check if we also have `(1, 5)` and `(5, 1)`. If we do, we have a candidate rectangle.

**Algorithm**

Put all the points in a set. For each pair of points, if the associated rectangle are 4 distinct points all in the set, then take the area of this rectangle as a candidate answer.

```python
class Solution(object):
    def minAreaRect(self, points):
        S = set(map(tuple, points))
        ans = float('inf')
        for j, p2 in enumerate(points):
            for i in xrange(j):
                p1 = points[i]
                if (p1[0] != p2[0] and p1[1] != p2[1] and
                        (p1[0], p2[1]) in S and (p2[0], p1[1]) in S):
                    ans = min(ans, abs(p2[0] - p1[0]) * abs(p2[1] - p1[1]))
        return ans if ans < float('inf') else 0
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the length of points.

* Space Complexity: $O(N)$, where $H$ is the height of the tree.

# Submissions
---
**Solution:**
```
Runtime: 708 ms
Memory Usage: 30.4 MB
```
```python
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        columns = collections.defaultdict(list)
        for x, y in points:
            columns[x].append(y)
        lastx = {}
        ans = float('inf')

        for x in sorted(columns):
            column = columns[x]
            column.sort()
            for j, y2 in enumerate(column):
                for i in range(j):
                    y1 = column[i]
                    if (y1, y2) in lastx:
                        ans = min(ans, (x - lastx[y1,y2]) * (y2 - y1))
                    lastx[y1, y2] = x
        return ans if ans < float('inf') else 0
```

**Solution:**
```
Runtime: 2396 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        S = set(map(tuple, points))
        ans = float('inf')
        for j, p2 in enumerate(points):
            for i in range(j):
                p1 = points[i]
                if (p1[0] != p2[0] and p1[1] != p2[1] and
                        (p1[0], p2[1]) in S and (p2[0], p1[1]) in S):
                    ans = min(ans, abs(p2[0] - p1[0]) * abs(p2[1] - p1[1]))
        return ans if ans < float('inf') else 0
```

**Solution 1: (Hash Table, brute force over every point pair)**

case 1:
    p0[0],p1[1]
    x       .
         /  p1
       /
    .       x
    p0      p1[0],p0[1]
 -> ^^
      
case 2:
            p0[0],p1[1]
    .       x 
    p1 \
         \
    x       .
p1[0],p0[1] p0
         -> ^^
```
Runtime: 155 ms, Beats 81.23%
Memory: 25.87 MB, Beats 55.96%
```
```c++
class Solution {
public:
    int minAreaRect(vector<vector<int>>& points) {
        int n = points.size(), i, j, ans = INT_MAX;
        unordered_map<int, unordered_set<int>> mp;
        for (i = 0; i < n; i ++) {
            mp[points[i][0]].insert(points[i][1]);
        }
        for (j = 1; j < n; j ++) {
            vector<int> &p0 = points[j];
            for (i = 0; i < j; i ++) {
                vector<int> &p1 = points[i];
                if (p0[0] != p1[0] && p0[1] != p1[1]) {
                    if (mp[p0[0]].count(p1[1]) && mp[p1[0]].count(p0[1])) {
                        ans = min(ans, abs(p0[0] - p1[0]) * abs(p0[1] - p1[1]));
                    }
                }
            }
        }
        return ans != INT_MAX ? ans : 0;
    }
};
```
