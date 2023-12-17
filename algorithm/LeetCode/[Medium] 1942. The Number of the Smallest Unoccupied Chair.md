1942. The Number of the Smallest Unoccupied Chair

There is a party where `n` friends numbered from `0` to `n - 1` are attending. There is an infinite number of chairs in this party that are numbered from `0` to infinity. When a friend arrives at the party, they sit on the unoccupied chair with the smallest number.

* For example, if chairs `0`, `1`, and `5` are occupied when a friend comes, they will sit on chair number `2`.

When a friend leaves the party, their chair becomes unoccupied at the moment they leave. If another friend arrives at that same moment, they can sit in that chair.

You are given a **0-indexed** 2D integer array `times` where `times[i] = [arrivali, leavingi]`, indicating the arrival and leaving times of the ith friend respectively, and an integer `targetFriend`. All arrival times are distinct.

Return the **chair number** that the friend numbered `targetFriend` will sit on.

 

**Example 1:**
```
Input: times = [[1,4],[2,3],[4,6]], targetFriend = 1
Output: 1
Explanation: 
- Friend 0 arrives at time 1 and sits on chair 0.
- Friend 1 arrives at time 2 and sits on chair 1.
- Friend 1 leaves at time 3 and chair 1 becomes empty.
- Friend 0 leaves at time 4 and chair 0 becomes empty.
- Friend 2 arrives at time 4 and sits on chair 0.
Since friend 1 sat on chair 1, we return 1.
```

**Example 2:**
```
Input: times = [[3,10],[1,5],[2,6]], targetFriend = 0
Output: 2
Explanation: 
- Friend 1 arrives at time 1 and sits on chair 0.
- Friend 2 arrives at time 2 and sits on chair 1.
- Friend 0 arrives at time 3 and sits on chair 2.
- Friend 1 leaves at time 5 and chair 0 becomes empty.
- Friend 2 leaves at time 6 and chair 1 becomes empty.
- Friend 0 leaves at time 10 and chair 2 becomes empty.
Since friend 0 sat on chair 2, we return 2.
```

**Constraints:**

* `n == times.length`
* `2 <= n <= 10^4`
* `times[i].length == 2`
* `1 <= arrivali < leavingi <= 10^5`
* `0 <= targetFriend <= n - 1`
* Each `arrivali` time is **distinct**.

# Submissions
---
**Solution 1: (Heap, 2 heap with list)**
```
Runtime: 2392 ms
Memory Usage: 20.2 MB
```
```python
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        arrivals = []
        departures = []
        for ind, (x, y) in enumerate(times):
            heappush(arrivals, (x, ind))
            heappush(departures, (y, ind))
        d = {}
        occupied = [0] * len(times)
        while True:
            if arrivals and departures and arrivals[0][0] < departures[0][0]:
                _, ind = heappop(arrivals)
                d[ind] = occupied.index(0)
                occupied[d[ind]] = 1
                if ind == targetFriend:
                    return d[ind]
            elif arrivals and departures and arrivals[0][0] >= departures[0][0]:
                _, ind = heappop(departures)
                occupied[d[ind]] = 0
```

**Solution 2: (multimap and set)**
```
Runtime: 196 ms
Memory: 60.8 MB
```
```c++
class Solution {
public:
    int smallestChair(vector<vector<int>>& times, int targetFriend) {
        int t_arrival = times[targetFriend][0];
        sort(begin(times), end(times));
        multimap<int, int> reserved;
        set<int> avail;
        for (auto &t : times) {
            while (!reserved.empty() && begin(reserved)->first <= t[0]) {
                avail.insert(begin(reserved)->second);
                reserved.erase(begin(reserved));
            }
            if (t[0] == t_arrival)
                break;
            if (avail.empty())
                reserved.insert({t[1], reserved.size()});
            else {
                reserved.insert({t[1], *begin(avail)});
                avail.erase(begin(avail));
            }
        }
        return avail.empty() ? reserved.size() : (*begin(avail));
    }
};
```

**Solution 3: (Heap)**
```
Runtime: 192 ms
Memory: 51.5 MB
```
```c++
class Solution {
public:
    int smallestChair(vector<vector<int>>& times, int targetFriend) {
        int t_arrival = times[targetFriend][0];
        sort(begin(times), end(times));
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        for (auto &t : times) {
            while (!pq.empty() && pq.top().first < t[0]) {
                pq.push({t[0], pq.top().second});
                pq.pop();
            }
            if (t[0] == t_arrival)
                break;         
            if (pq.empty() || pq.top().first > t[0])
                pq.push({t[1], pq.size()});
            else {
                pq.push({t[1], pq.top().second});
                pq.pop();
            }
        }
        return !pq.empty() && pq.top().first <= t_arrival ? pq.top().second : pq.size();
    }
};
```
