1288. Remove Covered Intervals

Given a list of intervals, remove all intervals that are covered by another interval in the list. Interval `[a,b)` is covered by interval `[c,d)` if and only if `c <= a` and `b <= d`.

After doing so, return the number of remaining intervals.

 

**Example 1:**
```
Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
```

**Constraints:**

* `1 <= intervals.length <= 1000`
* `0 <= intervals[i][0] < intervals[i][1] <= 10^5`
* `intervals[i] != intervals[j] for all i != j`

# Submissions
---
**Solution 1: (Sort)**
```
Runtime: 100 ms
Memory Usage: 13.1 MB
```
```python
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res = right = 0
        for i, j in sorted(intervals, key=lambda a: [a[0], -a[1]]):
            res += j > right
            right = max(right, j)
        return res
```

**Solution 2: (Sort, Stack)**
```
Runtime: 108 ms
Memory Usage: 29.4 MB
```
```c++
class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](vector<int> a, vector<int> b){
            if (a[0] == b[0])
                return a[1] >= b[1];
            return a[0] < b[0];
        });
        stack<vector<int>> stk;
        for (auto interval: intervals) {
            if (!stk.empty() && stk.top()[0] <= interval[0] && interval[1] <= stk.top()[1])
                continue;
            stk.push(interval);
        }
        return stk.size();
    }
};
```

**Solution 3: (Sort)**
```
Runtime: 27 ms
Memory Usage: 11.3 MB
```
```c++
class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        int n = intervals.size();
        int ans = 1;//one for a and b;
        int a = intervals[0][0], b=intervals[0][1];
        for(int i = 1; i < n; i++){
            if (intervals[i][0] > a && intervals[i][1] > b)
                ans++;
            if (intervals[i][1] > b) {//here removing the covered part
                a = intervals[i][0];
                b = intervals[i][1];
            }
        }
        return ans;
    }
};
```
