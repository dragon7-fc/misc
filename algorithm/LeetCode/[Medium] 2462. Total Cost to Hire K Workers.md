2462. Total Cost to Hire K Workers

You are given a **0-indexed** integer array `costs` where `costs[i]` is the cost of hiring the `i`th worker.

You are also given two integers `k` and `candidates`. We want to hire exactly `k` workers according to the following rules:

* You will run `k` sessions and hire exactly one worker in each session.
* In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.
    * For example, if `costs = [3,2,7,7,1,2]` and `candidates = 2`, then in the first hiring session, we will choose the `4`th worker because they have the lowest cost `[3,2,7,7,1,2]`.
    * In the second hiring session, we will choose `1`st worker because they have the same lowest cost as `4`th worker but they have the smallest index `[3,2,7,7,2]`. Please note that the indexing may be changed in the process.

* If there are fewer than `candidates` workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
* A worker can only be chosen once.

Return the total cost to hire exactly `k` workers.

 

**Example 1:**
```
Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
Output: 11
Explanation: We hire 3 workers in total. The total cost is initially 0.
- In the first hiring round we choose the worker from [17,12,10,2,7,2,11,20,8]. The lowest cost is 2, and we break the tie by the smallest index, which is 3. The total cost = 0 + 2 = 2.
- In the second hiring round we choose the worker from [17,12,10,7,2,11,20,8]. The lowest cost is 2 (index 4). The total cost = 2 + 2 = 4.
- In the third hiring round we choose the worker from [17,12,10,7,11,20,8]. The lowest cost is 7 (index 3). The total cost = 4 + 7 = 11. Notice that the worker with index 3 was common in the first and last four workers.
The total hiring cost is 11.
```

**Example 2:**
```
Input: costs = [1,2,4,1], k = 3, candidates = 3
Output: 4
Explanation: We hire 3 workers in total. The total cost is initially 0.
- In the first hiring round we choose the worker from [1,2,4,1]. The lowest cost is 1, and we break the tie by the smallest index, which is 0. The total cost = 0 + 1 = 1. Notice that workers with index 1 and 2 are common in the first and last 3 workers.
- In the second hiring round we choose the worker from [2,4,1]. The lowest cost is 1 (index 2). The total cost = 1 + 1 = 2.
- In the third hiring round there are less than three candidates. We choose the worker from the remaining workers [2,4]. The lowest cost is 2 (index 0). The total cost = 2 + 2 = 4.
The total hiring cost is 4.
```

**Constraints:**

* `1 <= costs.length <= 10^5`
* `1 <= costs[i] <= 10^5`
* `1 <= k, candidates <= costs.length`

# Submissions
---
**Solution 1: (Heap)**
```
Runtime: 2526 ms
Memory: 42.7 MB
```
```python
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        N = len(costs)
        first, last = candidates, N-candidates-1
        hq = [(c, i) for i, c in enumerate(costs[:candidates])]
        hq += [(c, i) for i, c in enumerate(costs[-candidates:], N-candidates)]
        hq = list(set(hq))
        heapq.heapify(hq)
        ans = 0
        while k > 0:
            c, i = heapq.heappop(hq)
            ans += c
            if first <= last:
                if i < first:
                    heapq.heappush(hq, (costs[first], first))
                    first += 1
                else:
                    heapq.heappush(hq, (costs[last], last))
                    last -= 1
            k -= 1
                
        return ans
```

**Solution 2: (Heap)**
```
Runtime: 206 ms
Memory: 72.8 MB
```
```c++
class Solution {
public:
    long long totalCost(vector<int>& costs, int k, int candidates) {
        priority_queue<int,vector<int>,greater<int>> pq1,pq2;
        long long ans=0;
        int cnt = 0,i=0,j=costs.size()-1;
        while(cnt<k){
            while(pq1.size()<candidates && i<=j) pq1.push(costs[i++]);
            while(pq2.size()<candidates && j>=i) pq2.push(costs[j--]);
            int a=pq1.size()>0?pq1.top():INT_MAX;
            int b=pq2.size()>0?pq2.top():INT_MAX;
            // cout<<a<<" "<<b<<"\n";
            if(a<=b){
                ans+=a;
                pq1.pop();
            }else{
                ans+=b;
                pq2.pop();
            }
            cnt++;
        }
        return ans;
    }
};
```
