983. Minimum Cost For Tickets

In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array `days`.  Each day is an integer from `1` to `365`.

Train tickets are sold in 3 different ways:

* a 1-day pass is sold for `costs[0]` dollars;
* a 7-day pass is sold for `costs[1]` dollars;
* a 30-day pass is sold for `costs[2]` dollars.

The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of `days`.

 

**Example 1:**

```
Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.
```

**Example 2:**

```
Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total you spent $17 and covered all the days of your travel.
```

**Note:**

1. `1 <= days.length <= 365`
1. `1 <= days[i] <= 365`
1. `days` is in strictly increasing order.
1. `costs.length == 3`
1. `1 <= costs[i] <= 1000`

# Solution
---
## Approach 1: Dynamic Programming (Day Variant)
**Intuition and Algorithm**

For each day, if you don't have to travel today, then it's strictly better to wait to buy a pass. If you have to travel today, you have up to 3 choices: you must buy either a 1-day, 7-day, or 30-day pass.

We can express those choices as a recursion and use dynamic programming. Let's say `dp(i)` is the cost to fulfill your travel plan from day i to the end of the plan. Then, if you have to travel today, your cost is:

$\text{dp}(i) = \min(\text{dp}(i+1) + \text{costs}[0], \text{dp}(i+7) + \text{costs}[1], \text{dp}(i+30) + \text{costs}[2])$

```python
from functools import lru_cache

class Solution:
    def mincostTickets(self, days, costs):
        dayset = set(days)
        durations = [1, 7, 30]

        @lru_cache(None)
        def dp(i):
            if i > 365:
                return 0
            elif i in dayset:
                return min(dp(i + d) + c
                           for c, d in zip(costs, durations))
            else:
                return dp(i + 1)

        return dp(1)
```

**Complexity Analysis**

* Time Complexity: $O(W)$, where $W = 365$ is the maximum numbered day in your travel plan.

* Space Complexity: $O(W)$.


## Approach 2: Dynamic Programming (Window Variant)
**Intuition and Algorithm**

As in Approach 1, we only need to buy a travel pass on a day we intend to travel.

Now, let `dp(i)` be the cost to travel from day `days[i]` to the end of the plan. If say, `j1` is the largest index such that `days[j1] < days[i] + 1`, `j7` is the largest index such that `days[j7] < days[i] + 7`, and `j30` is the largest index such that `days[j30] < days[i] + 30`, then we have:

$\text{dp}(i) = \min(\text{dp}(j1) + \text{costs}[0], \text{dp}(j7) + \text{costs}[1], \text{dp}(j30) + \text{costs}[2])$

```python
from functools import lru_cache

class Solution:
    def mincostTickets(self, days, costs):
        N = len(days)
        durations = [1, 7, 30]

        @lru_cache(None)
        def dp(i): # How much money to do days[i]+
            if i >= N: return 0

            ans = float('inf')
            j = i
            for c, d in zip(costs, durations):
                while j < N and days[j] < days[i] + d:
                    j += 1
                ans = min(ans, dp(j) + c)

            return ans

        return dp(0)
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the number of unique days in your travel plan.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution 1: (Dynamic Programming (Day Variant) Top-Down)**
```
Runtime: 48 ms
Memory Usage: 13.6 MB
```
```python
from functools import lru_cache

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dayset = set(days)
        durations = [1, 7, 30]

        @lru_cache(None)
        def dp(i):
            if i > 365:
                return 0
            elif i in dayset:
                return min(dp(i + d) + c
                           for c, d in zip(costs, durations))
            else:
                return dp(i + 1)

        return dp(1)
```

**Solution 2: (Dynamic Programming (Window Variant) Top-Down)**
```
Runtime: 44 ms
Memory Usage: 13.2 MB
```
```python
from functools import lru_cache

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        N = len(days)
        durations = [1, 7, 30]

        @lru_cache(None)
        def dp(i): # How much money to do days[i]+
            if i >= N: return 0

            ans = float('inf')
            j = i
            for c, d in zip(costs, durations):
                while j < N and days[j] < days[i] + d:
                    j += 1
                ans = min(ans, dp(j) + c)

            return ans
        
        return dp(0)
```

**Solution 3: (DP Bottom-Up)**
```
Runtime: 3 ms
Memory: 10.2 MB
```
```c++
class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        unordered_set<int> st(days.begin(), days.end());
        vector<int> dp(366);
        for (int i = days[0]; i <= days.back(); i ++) {
            if (st.count(i)) {
                dp[i] = min(min(dp[i-1]+costs[0], dp[max(0, i-7)]+costs[1]), dp[max(0, i-30)]+costs[2]);
            } else {
                dp[i] = dp[i-1];
            }
        }
        return dp[days.back()];
    }
};
```

**Solution 4: (DP Bottom-Up)**
```
Runtime: 4 ms
Memory: 9.6 MB
```
```c++
class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        int n = days.size();
        vector<int> dp(n + 1, INT_MAX);
        dp[0] = 0;
        for (int i = 1; i <= n; i++) {
            dp[i] = dp[i - 1] + costs[0]; // 1-day pass for current day
            
            int j = i - 1;
            while (j >= 0 && days[i - 1] - days[j] < 7) j--;
            dp[i] = min(dp[i], dp[j + 1] + costs[1]); // 7-day pass for current day
            
            j = i - 1;
            while (j >= 0 && days[i - 1] - days[j] < 30) j--;
            dp[i] = min(dp[i], dp[j + 1] + costs[2]); // 30-day pass for current day
        }
        
        return dp[n];
    }
};
```

**Solution 5: (DP Bottom-Up, deque)**
```
Runtime: 2 ms
Memory: 9.6 MB
```
```c++
class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        queue<pair<int, int>> last7, last30;
        int cost = 0;
        for (auto d : days) {
            while (!last7.empty() && last7.front().first + 7 <= d) last7.pop();
            while (!last30.empty() && last30.front().first + 30 <= d) last30.pop();
            last7.push({ d, cost + costs[1] });
            last30.push({ d, cost + costs[2] });
            cost = min({ cost + costs[0], last7.front().second, last30.front().second });
        }
        return cost;
    }
};
```

**Solution 6: (DP Bottom-Up)**

     1, 4, 6, 7, 8, 20
     ^i             ^j
dp   0  2 >4 >6  8 >9  11 
              9 11 13  19
             13 15 17  18
              7  9 11  17
             11 13 15  15
                >7 9   13
                11 13  11
                   11

    cost: [7,2,15]
        1,  4,  6,  7,  8,  20
    dp  0   

```
Runtime: 0 ms
Memory: 13.29 MB
```
```c++
class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        int n = days.size(), i, j;
        vector<int> dp(n+1);
        for (j = 0; j < n; j ++) {
            dp[j+1] = dp[j] + *min_element(costs.begin(), costs.end());
            for (i = j-1; i >= 0 && days[j]-days[i] < 30; i--) {
                if (days[j]-days[i] < 7) {
                    dp[j+1] = min(dp[j+1], dp[i] + costs[1]);
                }
                dp[j+1] = min(dp[j+1], dp[i] + costs[2]);
            }
        }
        return dp[n];
    }
};
```
