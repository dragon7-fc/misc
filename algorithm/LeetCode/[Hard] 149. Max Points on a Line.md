149. Max Points on a Line

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

**Example 1:**
```
Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
```

**Example 2:**
```
Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
```

**NOTE:** input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

# Submissions
---
**Solution 1: (Math, Hash Table)**
```
Runtime: 56 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2: return n

        points.sort()
        best = 0 # keep track of the best solution seen so far
        for i in range(n-1):
		    # For each point we'll traverse all those to the right of it in the sorted order and count on which line they lie
            duplicates = 0 # points with the same coordinates count towards all lines containing i
            horizontal = 0 # i and j form a line parallel with x-axis
            vertical = 0 # i and j form a line parallel with y-axis
            linecnt = collections.defaultdict(int) # i and j form a line different to the two above
            
            for j in range(i+1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                
                if dx == 0 and dy == 0:
                    duplicates += 1
                elif dx == 0:
                    vertical += 1
                elif dy == 0:
                    horizontal += 1
                else:
                    g = math.gcd(dx, dy)
                    slope = (dx/g, dy/g) # a canonical way to represent slope
                    linecnt[slope] += 1
                    
            max_other_points_on_line = max(list(linecnt.values()) + [horizontal, vertical])
            best = max(best, 1 + max_other_points_on_line + duplicates) # 1 stands for this point
                
        return best
```

**Solution 2: (Math, Hash Table)**
```
Runtime: 114 ms
Memory: 14.1 MB
```
```python
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1
        result = 2
        for i in range(n):
            cnt = collections.defaultdict(int)
            for j in range(n):
                if j != i:
                    cnt[math.atan2(points[j][1] - points[i][1],
                                   points[j][0] - points[i][0])] += 1
            result = max(result, max(cnt.values()) + 1)
        return result
```

**Solution 3: (Brute Force, Hash Table)**
```
Runtime: 32 ms, Beats 50.12%
Memory: 19.69 MB, Beats 41.58%
```
```c++
class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        int n = points.size(), i, j, xi, xj, yi, yj, ans = 2;
        double slope;
        if (n == 1) {
            return 1;
        }
        unordered_map<double, int> cnt;
        for (i = 0; i < n; i++) {
            xi = points[i][0];
            yi = points[i][1];
            cnt.clear();
            for (j = 0; j < n; j++) {
                if (j == i) {
                    continue;
                }
                xj = points[j][0];
                yj = points[j][1];
                if (xj == xi) {
                    slope = 100000;
                } else {
                    slope = (double)(yj - yi) / (xj - xi);
                }
                cnt[slope] += 1;
                ans = max(ans, cnt[slope] + 1);
            }
        }
        return ans;
    }
};
```
