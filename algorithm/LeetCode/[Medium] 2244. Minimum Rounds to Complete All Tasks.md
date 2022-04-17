2244. Minimum Rounds to Complete All Tasks

You are given a **0-indexed** integer array `tasks`, where `tasks[i]` represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the **same difficulty level**.

Return the **minimum** rounds required to complete all the tasks, or `-1` if it is not possible to complete all the tasks.

 

**Example 1:**
```
Input: tasks = [2,2,3,3,2,4,4,4,4,4]
Output: 4
Explanation: To complete all the tasks, a possible plan is:
- In the first round, you complete 3 tasks of difficulty level 2. 
- In the second round, you complete 2 tasks of difficulty level 3. 
- In the third round, you complete 3 tasks of difficulty level 4. 
- In the fourth round, you complete 2 tasks of difficulty level 4.  
It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.
```

**Example 2:**
```
Input: tasks = [2,3,3]
Output: -1
Explanation: There is only 1 task of difficulty level 2, but in each round, you can only complete either 2 or 3 tasks of the same difficulty level. Hence, you cannot complete all the tasks, and the answer is -1.
```

**Constraints:**

* `1 <= tasks.length <= 10^5`
* `1 <= tasks[i] <= 10^9`

# Submissions
---
**Solution 1: (Counter)**
```
Runtime: 1045 ms
Memory Usage: 28.4 MB
```
```python
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cnt = collections.Counter(tasks)
        ans = 0
        for _, v in cnt.items():
            if (v == 1):
                return -1
            d, r = divmod(v, 3)
            ans += d + (r > 0)
        return ans
```

**Solution 2: (Counter)**
```
Runtime: 222 ms
Memory Usage: 103.7 MB
```
```c++
class Solution {
public:
    int minimumRounds(vector<int>& tasks) {
        unordered_map<int, int> count;
        int res = 0, freq1;
        for (int a: tasks)
            ++count[a];
        for (auto& it: count) {
            if (it.second == 1) return -1;
            res += (it.second + 2) / 3;
        }
        return res;
    }
};
```
