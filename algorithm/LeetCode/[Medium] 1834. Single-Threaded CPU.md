1834. Single-Threaded CPU

You are given n tasks labeled from `0` to `n - 1` represented by a 2D integer array `tasks`, where `tasks[i] = [enqueueTimei, processingTimei]` means that the `i`th task will be available to process at `enqueueTimei` and will take `processingTimei` to finish processing.

You have a single-threaded CPU that can process **at most one** task at a time and will act in the following way:

* If the CPU is idle and there are no available tasks to process, the CPU remains idle.
* If the CPU is idle and there are available tasks, the CPU will choose the one with the **shortest processing time**. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
* Once a task is started, the CPU will **process the entire task** without stopping.
* The CPU can finish a task then start a new one instantly.

Return the order in which the CPU will process the tasks.

 

**Example 1:**
```
Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
Output: [0,2,3,1]
Explanation: The events go as follows: 
- At time = 1, task 0 is available to process. Available tasks = {0}.
- Also at time = 1, the idle CPU starts processing task 0. Available tasks = {}.
- At time = 2, task 1 is available to process. Available tasks = {1}.
- At time = 3, task 2 is available to process. Available tasks = {1, 2}.
- Also at time = 3, the CPU finishes task 0 and starts processing task 2 as it is the shortest. Available tasks = {1}.
- At time = 4, task 3 is available to process. Available tasks = {1, 3}.
- At time = 5, the CPU finishes task 2 and starts processing task 3 as it is the shortest. Available tasks = {1}.
- At time = 6, the CPU finishes task 3 and starts processing task 1. Available tasks = {}.
- At time = 10, the CPU finishes task 1 and becomes idle.
```

**Example 2:**
```
Input: tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
Output: [4,3,2,0,1]
Explanation: The events go as follows:
- At time = 7, all the tasks become available. Available tasks = {0,1,2,3,4}.
- Also at time = 7, the idle CPU starts processing task 4. Available tasks = {0,1,2,3}.
- At time = 9, the CPU finishes task 4 and starts processing task 3. Available tasks = {0,1,2}.
- At time = 13, the CPU finishes task 3 and starts processing task 2. Available tasks = {0,1}.
- At time = 18, the CPU finishes task 2 and starts processing task 0. Available tasks = {1}.
- At time = 28, the CPU finishes task 0 and starts processing task 1. Available tasks = {}.
- At time = 40, the CPU finishes task 1 and becomes idle.
```

**Constraints:**

* `tasks.length == n`
* `1 <= n <= 10^5`
* `1 <= enqueueTimei, processingTimei <= 10^9`

# Submissions
---
**Solution 1: (Heap)**
```
Runtime: 2060 ms
Memory: 63.6 MB
```
```python
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Sort based on min task processing time or min task index.
        next_task: List[Tuple[int, int]] = []
        tasks_processing_order: List[int] = []
        
        # Store task enqueue time, processing time, index.
        sorted_tasks = [(enqueue, process, idx) for idx, (enqueue, process) in enumerate(tasks)]
        sorted_tasks.sort()
        
        curr_time = 0
        task_index = 0
        
        # Stop when no tasks are left in array and heap.
        while task_index < len(tasks) or next_task:
            if not next_task and curr_time < sorted_tasks[task_index][0]:
                # When the heap is empty, try updating curr_time to next task's enqueue time. 
                curr_time = sorted_tasks[task_index][0]
            
            # Push all the tasks whose enqueueTime <= currtTime into the heap.
            while task_index < len(sorted_tasks) and curr_time >= sorted_tasks[task_index][0]:
                _, process_time, original_index = sorted_tasks[task_index]
                heapq.heappush(next_task, (process_time, original_index))
                task_index += 1
            
            process_time, index = heapq.heappop(next_task)
            
            # Complete this task and increment curr_time.
            curr_time += process_time
            tasks_processing_order.append(index)
        
        return tasks_processing_order
```

**Solution 2: (Heap, Greedy)**
```
Runtime: 2377 ms
Memory: 61.7 MB
```
```python
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        N = len(tasks)
        sorted_task = sorted([[t, p, i] for i, [t, p] in enumerate(tasks)])
        j = 1
        hq = [[sorted_task[0][1], sorted_task[0][2], sorted_task[0][0]]]
        cur = 0
        ans = []
        while hq:
            process, i, t = heapq.heappop(hq)
            ans += [i]
            cur = max(cur, t)
            cur += process
            if not hq and j < N:
                cur = max(cur, sorted_task[j][0])
            while j < N and sorted_task[j][0] <= cur:
                heapq.heappush(hq, [sorted_task[j][1], sorted_task[j][2], sorted_task[j][0]])
                j += 1
        return ans
```

**Solution 3: (Heap, sort then greedy over min heap with current time)**

3            --    
2         -----
1      -----------
0   -----
    1  2  3  4  5  6  7  8
cur ^     ^     ^  ^
pq  0     12    13 1
    x      x     x x
    --------
          --------
                -----
ans 0     2     3  1

4                           ------
3                           ---------------
2                           --------------------
1                           --------------------------------------------------------
0                           ---------------------------------------------
    1   2   3   4   5   6   7   8   9   10   11   12   13   14   15   16   17   18
cur                         ^       ^                   ^
pq                          01234   0123               012
                                x      x                 x
                            ----------
                                    ----------------------
                                                       ----------------------------------
ans                         4       3                  2
```
Runtime: 75 ms, Beats 92.82%
Memory: 130.91 MB, Beats 87.54%
```
```c++
class Solution {
public:
    vector<int> getOrder(vector<vector<int>>& tasks) {
        int n = tasks.size(), i;
        long long cur = 0;
        vector<int> ans;
        vector<tuple<int,int,int>> dp;
        for (i = 0; i < n; i ++) {
            dp.push_back({tasks[i][0], tasks[i][1], i});
        }
        sort(dp.begin(), dp.end());
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
        cur = 0;
        pq.push({get<1>(dp[0]), get<2>(dp[0])});
        i = 1;
        while (pq.size()) {
            auto [p, j] = pq.top();
            pq.pop();
            ans.push_back(j);
            cur = max(cur, (long long)tasks[j][0]);
            while (i < n && get<0>(dp[i]) <= cur + p) {
                pq.push({get<1>(dp[i]), get<2>(dp[i])});
                i += 1;
            }
            cur += p;
            if (pq.size() == 0 && i < n) {
                pq.push({get<1>(dp[i]), get<2>(dp[i])});
                cur = get<0>(dp[i]);
                i += 1;
            }
        }
        return ans;
    }
};
```
