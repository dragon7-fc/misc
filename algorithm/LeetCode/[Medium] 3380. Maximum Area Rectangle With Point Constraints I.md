3380. Maximum Area Rectangle With Point Constraints I

You are given an array `points` where `points[i] = [xi, yi]` represents the coordinates of a point on an infinite plane.

Your task is to find the **maximum** area of a rectangle that:

* Can be formed using **four** of these points as its corners.
* Does **not** contain any other point inside or on its border.
* Has its edges **parallel** to the axes.

Return the **maximum** area that you can obtain or `-1` if no such rectangle is possible.

 

**Example 1:**
```
Input: points = [[1,1],[1,3],[3,1],[3,3]]

Output: 4

Explanation:
```
![3380_example1.png](img/3380_example1.png)
```
We can make a rectangle with these 4 points as corners and there is no other point that lies inside or on the border. Hence, the maximum possible area would be 4.
```

**Example 2:**
```
Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]

Output: -1

Explanation:
```
![3380_example2.png](img/3380_example2.png)
```
There is only one rectangle possible is with points [1,1], [1,3], [3,1] and [3,3] but [2,2] will always lie inside it. Hence, returning -1.
```

**Example 3:**
```
Input: points = [[1,1],[1,3],[3,1],[3,3],[1,2],[3,2]]

Output: 2

Explanation:
```
![3380_example3.png](img/3380_example3.png)
```
The maximum area rectangle is formed by the points [1,3], [1,2], [3,2], [3,3], which has an area of 2. Additionally, the points [1,1], [1,2], [3,1], [3,2] also form a valid rectangle with the same area.
```
 

**Constraints:**

* `1 <= points.length <= 10`
* `points[i].length == 2`
* `0 <= xi, yi <= 100`
* All the given points are **unique**.

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 3 ms
Memory: 33.04 MB
```
```c++
class Solution {
public:
    int maxRectangleArea(vector<vector<int>>& points) {
        int n = points.size(), i, j, k, l, x, y, x2, y2, x3, y3, cnt[101][101] = {0}, ans = -1;
        bool flag;
        for (auto p: points) {
            cnt[p[0]][p[1]] += 1;
        }
        sort(points.begin(), points.end());
        for (i = 0; i < n-3; i ++) {
            for (j = i+1; j < n-2; j ++) {
                for (k = j+1; k < n-1; k ++) {
                    for (l = k+1; l < n; l ++) {
                        if (points[i][0] == points[j][0] && points[k][0] == points[l][0] && points[i][1] == points[k][1] && points[j][1] == points[l][1])  {
                            flag = true;
                            x = points[i][0], y = points[i][1], x2 = points[l][0], y2 = points[l][1];
                            for (x3 = x+1; x3 < x2; x3++) {
                                if (cnt[x3][y] || cnt[x3][y2]) {
                                    flag = false;
                                    break;
                                }
                            }
                            if (!flag) {
                                break;
                            }
                            for (y3 = y+1; y3 < y2; y3++) {
                                if (cnt[x][y3] || cnt[x2][y3]) {
                                    flag = false;
                                    break;
                                }
                            }
                            if (!flag) {
                                break;
                            }
                            for (x3 = x+1; x3 < x2; x3++) {
                                for (y3 = y+1; y3 < y2; y3++) {
                                    if (cnt[x3][y3]) {
                                        flag = false;
                                        break;
                                    }
                                }
                                if (!flag) {
                                    break;
                                }
                            }
                            if (!flag) {
                                break;
                            }
                            ans = max(ans, (x2-x)*(y2-y));
                        }
                    }
                }
            }
        }
        return ans;
    }
};
```
