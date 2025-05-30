1882. Process Tasks Using Servers

You are given two **0-indexed** integer arrays servers and tasks of lengths `n` and `m` respectively. `servers[i]` is the **weight** of the `i`th server, and `tasks[j]` is the **time needed** to process the `j`th task **in seconds**.

You are running a simulation system that will shut down after all tasks are processed. Each server can only process one task at a time. You will be able to process the `j`th task starting from the `j`th second beginning with the `0`th task at second `0`. To process task `j`, you assign it to the server with the smallest weight that is free, and in case of a tie, choose the server with the smallest index. If a free server gets assigned task `j` at second `t`, it will be free again at the second `t + tasks[j]`.

If there are no free servers, you must wait until one is free and execute the free tasks **as soon as possible**. If **multiple** tasks need to be assigned, assign them in order of **increasing index**s.

You may assign multiple tasks at the same second if there are multiple free servers.

Build an array `ans` of length `m`, where `ans[j]` is the **index** of the server the `j`th task will be assigned to.

Return the array `ans`.

 

**Example 1:**
```
Input: servers = [3,3,2], tasks = [1,2,3,2,1,2]
Output: [2,2,0,2,1,2]
Explanation: Events in chronological order go as follows:
- At second 0, task 0 is added and processed using server 2 until second 1.
- At second 1, server 2 becomes free. Task 1 is added and processed using server 2 until second 3.
- At second 2, task 2 is added and processed using server 0 until second 5.
- At second 3, server 2 becomes free. Task 3 is added and processed using server 2 until second 5.
- At second 4, task 4 is added and processed using server 1 until second 5.
- At second 5, all servers become free. Task 5 is added and processed using server 2 until second 7.
```

**Example 2:**
```
Input: servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]
Output: [1,4,1,4,1,3,2]
Explanation: Events in chronological order go as follows: 
- At second 0, task 0 is added and processed using server 1 until second 2.
- At second 1, task 1 is added and processed using server 4 until second 2.
- At second 2, servers 1 and 4 become free. Task 2 is added and processed using server 1 until second 4. 
- At second 3, task 3 is added and processed using server 4 until second 7.
- At second 4, server 1 becomes free. Task 4 is added and processed using server 1 until second 9. 
- At second 5, task 5 is added and processed using server 3 until second 7.
- At second 6, task 6 is added and processed using server 2 until second 7.
```

**Constraints:**

* `servers.length == n`
* `tasks.length == m`
* `1 <= n, m <= 2 * 10^5`
* `1 <= servers[i], tasks[j] <= 2 * 10^5`

# Submissions
---
**Solution 1: (Heap, 2 heap)**
```
Runtime: 2100 ms
Memory Usage: 62.9 MB
```
```python
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        servers_available = [(w, i) for i,w in enumerate(servers)]
        heapify(servers_available)
        tasks_in_progress = []
        res = []
        time = 0
        for j,task in enumerate(tasks):
            time = max(time, j)
            if not servers_available:
                time = tasks_in_progress[0][0]
            while tasks_in_progress and tasks_in_progress[0][0] <= time:
                heappush(servers_available, heappop(tasks_in_progress)[1])
            res.append(servers_available[0][1])
            heappush(tasks_in_progress, (time + task, heappop(servers_available)))
        return res
```

**Solution 2: (Heap, 2 heap)**

    servers = [3,3,2],
    tasks = [1,   2,   3,   2,   1,   2]
                                 ^
pq           332  332  33_  _32  _3_  _32
               x    x  x      x   x     x
                              
    servers = [5,1,4,3,2],
    tasks = [2,    1,    2,    4,    5,    2,    1]
pq           51432 5_432 51432 5_432 5143_ 5_43_ 5_4__   32       1
              x        x  x        x  x       x    x

```
Runtime: 371 ms
Memory: 126.4 MB
```
```c++
class Solution {
public:
    vector<int> assignTasks(vector<int>& servers, vector<int>& tasks) {
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;  // {weight, i}, free
        priority_queue<pair<int,pair<int,int>>, vector<pair<int,pair<int,int>>>, greater<pair<int,pair<int,int>>>> dp;  // {time, {weight, i}}, working
        int cur = 0;
        vector<int> ans;
        for (int i = 0; i < servers.size(); i ++) {
            pq.push({servers[i], i});
        }
        for (int i = 0; i < tasks.size(); i ++) {
            cur = max(cur, i);
            if (pq.empty()) {
                pq.push(dp.top().second);
                cur = max(cur, dp.top().first);
                dp.pop();
            }
            while (dp.size() && dp.top().first <= cur) {
                auto [_, p] = dp.top();
                dp.pop();
                pq.push(p);
            }
            auto p = pq.top();
            ans.push_back(p.second);
            dp.push({cur + tasks[i], p});
            pq.pop();
        }
        return ans;
    }
};
```
