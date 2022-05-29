2285. Maximum Total Importance of Roads

You are given an integer `n` denoting the number of cities in a country. The cities are numbered from `0` to `n - 1`.

You are also given a 2D integer array `roads` where `roads[i]` = `[ai, bi]` denotes that there exists a **bidirectional** road connecting cities `ai` and `bi`.

You need to assign each city with an integer value from `1` to `n`, where each value can only be used **once**. The **importance** of a road is then defined as the **sum** of the values of the two cities it connects.

Return the **maximum total importance** of all roads possible after assigning the values optimally.

 

**Example 1:**

![2285_ex1drawio.png](img/2285_ex1drawio.png)
```
Input: n = 5, roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
Output: 43
Explanation: The figure above shows the country and the assigned values of [2,4,5,3,1].
- The road (0,1) has an importance of 2 + 4 = 6.
- The road (1,2) has an importance of 4 + 5 = 9.
- The road (2,3) has an importance of 5 + 3 = 8.
- The road (0,2) has an importance of 2 + 5 = 7.
- The road (1,3) has an importance of 4 + 3 = 7.
- The road (2,4) has an importance of 5 + 1 = 6.
The total importance of all roads is 6 + 9 + 8 + 7 + 7 + 6 = 43.
It can be shown that we cannot obtain a greater total importance than 43.
```

**Example 2:**

![2285_ex2drawio.png](img/2285_ex2drawio.png)
```
Input: n = 5, roads = [[0,3],[2,4],[1,3]]
Output: 20
Explanation: The figure above shows the country and the assigned values of [4,3,2,5,1].
- The road (0,3) has an importance of 4 + 5 = 9.
- The road (2,4) has an importance of 2 + 1 = 3.
- The road (1,3) has an importance of 3 + 5 = 8.
The total importance of all roads is 9 + 3 + 8 = 20.
It can be shown that we cannot obtain a greater total importance than 20.
```

**Constraints:**

* `2 <= n <= 5 * 10^4`
* `1 <= roads.length <= 5 * 10^4`
* `roads[i].length == 2`
* `0 <= ai, bi <= n - 1`
* `ai != bi`
* There are no duplicate roads.

# Submissions
---
**Solution 1: (Node Degree)**
```
Runtime: 1620 ms
Memory Usage: 39.6 MB
```
```python
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
        return sum((i + 1) * d for i, d in enumerate(sorted(degree)))
```

**Solution 2: (Node Degree)**
```
Runtime: 509 ms
Memory Usage: 111.7 MB
```
```c++
class Solution {
public:
    long long maximumImportance(int n, vector<vector<int>>& roads) {
        long long cnt[50001] = {}, res = 0;
        for (auto &r : roads) {
            ++cnt[r[0]];
            ++cnt[r[1]];
        }
        sort(begin(cnt), begin(cnt) + n);
        for (int i = 0; i < n; ++i)
            res += cnt[i] * (i + 1);
        return res;
    }
};
```
