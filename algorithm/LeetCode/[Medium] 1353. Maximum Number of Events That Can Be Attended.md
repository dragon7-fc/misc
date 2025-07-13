1353. Maximum Number of Events That Can Be Attended

Given an array of `events` where `events[i] = [startDayi, endDayi]`. Every event `i` starts at `startDayi` and ends at `endDayi`.

You can attend an event `i` at any day `d` where `startTimei <= d <= endTimei`. Notice that you can only attend one event at any time `d`.

Return the maximum number of events you can attend.

 

**Example 1:**

![1353_e1.png](img/1353_e1.png)
```
Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.
```

**Example 2:**
```
Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4
```

**Example 3:**
```
Input: events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
Output: 4
```

**Example 4:**
```
Input: events = [[1,100000]]
Output: 1
```

**Example 5:**
```
Input: events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
Output: 7
```

**Constraints:**

* `1 <= events.length <= 10^5`
* `events[i].length == 2`
* `1 <= events[i][0] <= events[i][1] <= 10^5`

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 852 ms
Memory Usage: 50.4 MB
```
```python
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda item: (item[1], item[0]))
        days = set()
        for start, end in events:
            if start not in days:
                days.add(start)
            else:
                i = start + 1
                while i in days and i <= end:
                    i += 1
                if i <= end:
                    days.add(i)
        return len(days)         
```

**Solution 2: (Heap)**
```
Runtime: 908 ms
Memory Usage: 47.7 MB
```
```python
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        heapq.heapify(events)
        ans = 0
        day = 1
        while events:
            start, end = heapq.heappop(events)
            if start>=day:
                ans += 1
                day = start + 1
            elif day<=end:
                heapq.heappush(events, [day,end])
        return ans
```

**Solution 3: (Heap)**
```
Runtime: 59 ms, Beats 79.86%
Memory: 75.03 MB, Beats 39.30%
```
```c++
class Solution {
public:
    int maxEvents(vector<vector<int>>& events) {
        int n = events.size(), i, j = 0, mx = 0,ans = 0;
        for (i = 0; i < n; i ++) {
            mx = max(mx, events[i][1]);
        }
        priority_queue<int,vector<int>,greater<>> pq;
        sort(events.begin(), events.end());
        for (i = events[0][0]; i <= mx; i ++) {
            while (j < n && events[j][0] <= i) {
                pq.push(events[j][1]);
                j += 1;
            }
            while (pq.size() && pq.top() < i) {
                pq.pop();
            }
            if (pq.size()) {
                pq.pop();
                ans += 1;
            }
        }
        return ans;
    }
};
```

**Solution 4: (Heap)**
```
Runtime: 61 ms, Beats 64.28%
Memory: 74.79 MB, Beats 98.35%
```
```c++
class Solution {
public:
    int maxEvents(vector<vector<int>>& events) {
        int n = events.size(), i, j = 0,ans = 0;
        priority_queue<int,vector<int>,greater<>> pq;
        sort(events.begin(), events.end());
        while (pq.size() || j < n) {
            if (pq.size() == 0) {
                i = events[j][0];
            }
            while (j < n && events[j][0] == i) {
                pq.push(events[j][1]);
                j += 1;
            }
            pq.pop();
            ans += 1;
            i += 1;
            while (pq.size() && pq.top() < i) {
                pq.pop();
            }
        }
        return ans;
    }
};
```
