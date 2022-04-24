2250. Count Number of Rectangles Containing Each Point

You are given a 2D integer array `rectangles` where `rectangles[i] = [li, hi]` indicates that `i`th rectangle has a length of `li` and a height of `hi`. You are also given a 2D integer array `points` where `points[j] = [xj, yj]` is a point with coordinates `(xj, yj)`.

The `i`th rectangle has its **bottom-left corner** point at the coordinates `(0, 0)` and its **top-right corner** point at `(li, hi)`.

Return an integer array `count` of length `points.length` where `count[j]` is the number of rectangles that **contain** the `j`th point.

The `i`th rectangle **contains** the `j`th point if `0 <= xj <= li` and `0 <= yj <= hi`. Note that points that lie on the **edges** of a rectangle are also considered to be contained by that rectangle.

 

**Example 1:**

![2250_example1.png](img/2250_example1.png)
```
Input: rectangles = [[1,2],[2,3],[2,5]], points = [[2,1],[1,4]]
Output: [2,1]
Explanation: 
The first rectangle contains no points.
The second rectangle contains only the point (2, 1).
The third rectangle contains the points (2, 1) and (1, 4).
The number of rectangles that contain the point (2, 1) is 2.
The number of rectangles that contain the point (1, 4) is 1.
Therefore, we return [2, 1].
```

**Example 2:**

!{2250_example2.png](img/2250_example2.png)
```
Input: rectangles = [[1,1],[2,2],[3,3]], points = [[1,3],[1,1]]
Output: [1,3]
Explanation:
The first rectangle contains only the point (1, 1).
The second rectangle contains only the point (1, 1).
The third rectangle contains the points (1, 3) and (1, 1).
The number of rectangles that contain the point (1, 3) is 1.
The number of rectangles that contain the point (1, 1) is 3.
Therefore, we return [1, 3].
```

**Constraints:**

* `1 <= rectangles.length, points.length <= 5 * 10^4`
* `rectangles[i].length == points[j].length == 2`
* `1 <= li, xj <= 10^9`
* `1 <= hi, yj <= 100`
* All the `rectangles` are **unique**.
* All the `points` are **unique**.

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 2117 ms
Memory Usage: 35.8 MB
```
```python
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        from bisect import bisect
        
        rectangles = sorted(rectangles, key=lambda x:x[0])

        rectangle_map = defaultdict(list)

        for l, h in rectangles:
            rectangle_map[h].append(l)

        def contains(x, y):
            count = 0

            for height, widths in rectangle_map.items():
                if height >= y:
                    count += len(widths) - bisect(widths, x - 1)

            return count

        res = []

        for point in points:
            x, y = point
            res.append(contains(x, y))

        return res
```

**Solution 2: (Binary Search)**
```
Runtime: 1330 ms
Memory Usage: 85.1 MB
```
```c++
class Solution {
public:
    vector<int> countRectangles(vector<vector<int>>& rectangles, vector<vector<int>>& points) {
        vector<vector<int>> umap(101);
        for (auto &r: rectangles) {
            umap[r[1]].push_back(r[0]);
        }
        
        for (int i = 0; i < 101; i++) {
            sort(begin(umap[i]), end(umap[i]));
        }
        
        vector<int> res;
        for (auto &p: points) {
            int sum = 0;
            for (int i = p[1]; i < 101; i++) {
                auto lb = lower_bound(begin(umap[i]), end(umap[i]), p[0]);
                sum += end(umap[i]) - lb;
            }
            res.push_back(sum);
        }
        return res;
    }
};
```
