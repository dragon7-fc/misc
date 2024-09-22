539. Minimum Time Difference

Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.

**Example 1:**
```
Input: ["23:59","00:00"]
Output: 1
```

**Note:**

* The number of time points in the given list is at least `2` and won't exceed `20000`.
* The input time is legal and ranges from `00:00` to `23:59`.

# Submissions
---
**Solution 1: (String, Sort)**
```
Runtime: 68 ms
Memory Usage: 15.7 MB
```
```python
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timeInM = sorted([int(v[:2])*60 + int(v[3:]) for v in timePoints])
        min_diff = timeInM[0] - timeInM[-1] + 24*60
        for i in range(len(timeInM)-1):
            min_diff = min(timeInM[i+1] - timeInM[i] , min_diff)
            
        return min_diff
```

**Solution 2: (String, Sort)**
```
Runtime: 4 ms
Memory: 17.61 MB
```
```c++
class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        vector<int> dp;
        int h, m;
        for (auto t: timePoints) {
            h = (t[0]-'0')*10 + t[1]-'0';
            m = (t[3]-'0')*10 + t[4]-'0';
            dp.push_back(h*60 + m);
        }
        sort(dp.begin(), dp.end());
        int ans = 60*24+dp[0] - dp.back();
        for (int i = 1; i < dp.size(); i ++) {
            ans = min(ans, dp[i]-dp[i-1]);
        }
        return ans;
    }
};
```

**Solution 3: (Bucket Sort)**
```
Runtime: 9 ms
Memory: 17.38 MB
```
```c++
class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        // create buckets array for the times converted to minutes
        vector<bool> minutes(24 * 60, false);
        for (string time : timePoints) {
            int h = stoi(time.substr(0, 2));
            int m = stoi(time.substr(3));
            int min = h * 60 + m;
            if (minutes[min]) return 0;
            minutes[min] = true;
        }
        int prevIndex = INT_MAX;
        int firstIndex = INT_MAX;
        int lastIndex = INT_MAX;
        int ans = INT_MAX;

        // find differences between adjacent elements in sorted array
        for (int i = 0; i < 24 * 60; i++) {
            if (minutes[i]) {
                if (prevIndex != INT_MAX) {
                    ans = min(ans, i - prevIndex);
                }
                prevIndex = i;
                if (firstIndex == INT_MAX) {
                    firstIndex = i;
                }
                lastIndex = i;
            }
        }

        return min(ans, 24 * 60 - lastIndex + firstIndex);
    }
};
```
