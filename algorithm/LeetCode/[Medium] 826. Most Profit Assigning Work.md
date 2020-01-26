826. Most Profit Assigning Work

We have jobs: `difficulty[i]` is the difficulty of the `i`th job, and `profit[i]` is the profit of the `i`th job. 

Now we have some workers. `worker[i]` is the ability of the `i`th worker, which means that this worker can only complete a job with difficulty at most worker[i]. 

Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if 3 people attempt the same job that pays $1, then the total profit will be $3.  If a worker cannot complete any job, his profit is $0.

What is the most profit we can make?

**Example 1:**
```
Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100 
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get profit of [20,20,30,30] seperately.
```

**Notes:**

* `1 <= difficulty.length = profit.length <= 10000`
* `1 <= worker.length <= 10000`
* `difficulty[i]`, `profit[i]`, `worker[i]` are in range `[1, 10^5]`

# Submissions
---
**Solution 1: (Greedy, Binary search)**
```
Runtime: 460 ms
Memory Usage: 15 MB
```
```python
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = [[-1, 0]] + sorted([a, b] for a, b in zip(difficulty, profit))
        for i in range(1, len(jobs)):
            jobs[i][1] = max(jobs[i][1], jobs[i-1][1])
        return sum(jobs[bisect.bisect(jobs, [w, float('inf')]) - 1][1] for w in worker)
```

**Solution 2: (Greedy, Two pointer)**
```
Runtime: 372 ms
Memory Usage: 15.6 MB
```
```python
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(list(zip(difficulty, profit)), key=lambda x: x[0])
        jobs_key = [job[0] for job in jobs]
        N = len(jobs)
        ans = 0
        lastExploredTask = 0
        lastProfit = 0
        for ability in sorted(worker):
            while lastExploredTask < N and ability >= jobs_key[lastExploredTask]:
                currProfit = jobs[lastExploredTask][1]
                if currProfit > lastProfit:
                    lastProfit = currProfit
                lastExploredTask += 1
            ans += lastProfit
        return ans
```