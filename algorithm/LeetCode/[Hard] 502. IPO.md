502. IPO

Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most **k** distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most **k** distinct projects.

You are given several projects. For each project i, it has a pure profit **Pi** and a minimum capital of **Ci** is needed to start the corresponding project. Initially, you have **W** capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

To sum up, pick a list of at most **k** distinct projects from given projects to maximize your final capital, and output your final maximized capital.

**Example 1:**
```
Input: k=2, W=0, Profits=[1,2,3], Capital=[0,1,1].

Output: 4

Explanation: Since your initial capital is 0, you can only start the project indexed 0.
             After finishing it you will obtain profit 1 and your capital becomes 1.
             With capital 1, you can either start the project indexed 1 or the project indexed 2.
             Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
             Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
```

**Note:**

* You may assume all numbers in the input are non-negative integers.
* The length of `Profits` array and `Capital` array will not exceed `50,000`.
* The answer is guaranteed to fit in a `32`-bit signed integer.

# Submissions
---
**Solution 1: (Greedy, Heap, Sort)**
```
Runtime: 224 ms
Memory Usage: 20.9 MB
```
```python
class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        projects = sorted(zip(Capital, Profits))[::-1]
        currProfit = W
        heap = []
        for _ in range(k):
            while projects and currProfit >= projects[-1][0]:
                heapq.heappush(heap, -projects.pop()[1])
            if heap:
                currProfit += -heapq.heappop(heap)
        
        return currProfit
```

**Solution 2: (Greedy, Heap, Sort)**
```
Runtime: 233 ms
Memory: 82 MB
```
```c++
class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        int n = profits.size();
        vector<pair<int, int>> projects;
        for (int i = 0; i < n; i++) {
            projects.emplace_back(capital[i], profits[i]);
        }
        sort(projects.begin(), projects.end());
        priority_queue<int> q;
        int ptr = 0;
        for (int i = 0; i < k; i++) {
            while (ptr < n && projects[ptr].first <= w) {
                q.push(projects[ptr++].second);
            }
            if (q.empty()) {
                break;
            }
            w += q.top();
            q.pop();
        }
        return w;
    }
};
```
