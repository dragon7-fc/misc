252. Meeting Rooms

Given an array of meeting time intervals where `intervals[i] = [starti, endi]`, determine if a person could attend all meetings.

 

**Example 1:**
```
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
```

**Example 2:**
```
Input: intervals = [[7,10],[2,4]]
Output: true
```

**Constraints:**

* `0 <= intervals.length <= 10^4`
* `intervals[i].length == 2`
* `0 <= starti < endi <= 106`

# Submissions
---
**Solution 1: (Sorting)**
```
Runtime: 76 ms
Memory Usage: 17.5 MB
```
```python
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True
```

**Solution 1: (Sorting)**
```
Runtime: 12 ms
Memory Usage: 11.7 MB
```
```c++
class Solution {
public:
    bool canAttendMeetings(vector<vector<int>>& intervals) {
        if (intervals.empty()) {
            return true;
        }

        // Note: C++ sort function automatically sorts a vector first
        // by the 1st element, then by the 2nd element and so on.
        sort(intervals.begin(), intervals.end());
        for (size_t i = 0; i < intervals.size() - 1; i++) {
            if (intervals[i][1] > intervals[i + 1][0]) {
                return false;
            }
        }
        return true;
    }
};
```