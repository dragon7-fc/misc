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
Runtime: 24 ms
Memory Usage: 13.7 MB
```
```c++
class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        vector<int>dp;
        for (auto x: timePoints) {
            string hr = x.substr(0,2);
            string str = x.substr(3);
            int hrx = stoi(hr);
            int xy = stoi(str);
            xy = xy + hrx*60;
            dp.push_back(xy);
        }
        sort(dp.begin(), dp.end());
        int answer = INT_MAX;
        for (int i = 0; i < dp.size()-1; i++) {
           answer = min(answer, abs(dp[i] - dp[i+1]));
        }
        answer = min(answer, dp[0]+24*60-dp.back());
        return answer;
    }
};
```
