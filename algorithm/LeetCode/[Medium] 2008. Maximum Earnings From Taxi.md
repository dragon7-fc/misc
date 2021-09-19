2008. Maximum Earnings From Taxi

There are `n` points on a road you are driving your taxi on. The `n` points on the road are labeled from `1` to `n` in the direction you are going, and you want to drive from point `1` to point `n` to make money by picking up passengers. You cannot change the direction of the taxi.

The passengers are represented by a **0-indexed** 2D integer array `rides`, where `rides[i] = [starti, endi, tipi]` denotes the `i`th passenger requesting a ride from point `starti` to point `endi` who is willing to give a `tipi` dollar tip.

For each passenger `i` you pick up, you earn `endi - starti + tipi` dollars. You may only drive at most one passenger at a time.

Given `n` and `rides`, return the **maximum** number of dollars you can earn by picking up the passengers optimally.

**Note:** You may drop off a passenger and pick up a different passenger at the same point.

 

**Example 1:**
```
Input: n = 5, rides = [[2,5,4],[1,5,1]]
Output: 7
Explanation: We can pick up passenger 0 to earn 5 - 2 + 4 = 7 dollars.
```

**Example 2:**
```
Input: n = 20, rides = [[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]]
Output: 20
Explanation: We will pick up the following passengers:
- Drive passenger 1 from point 3 to point 10 for a profit of 10 - 3 + 2 = 9 dollars.
- Drive passenger 2 from point 10 to point 12 for a profit of 12 - 10 + 3 = 5 dollars.
- Drive passenger 5 from point 13 to point 18 for a profit of 18 - 13 + 1 = 6 dollars.
We earn 9 + 5 + 6 = 20 dollars in total.
```

**Constraints:**

* `1 <= n <= 10^5`
* `1 <= rides.length <= 3 * 10^4`
* `rides[i].length == 3`
* `1 <= starti < endi <= n`
* `1 <= tipi <= 10^5`

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 1648 ms
Memory Usage: 28.8 MB
```
```python
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        dp = [0] * (n + 1)
        rides.sort()
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1]
            while rides and i == rides[-1][0]:
                s, e, t = rides.pop()
                dp[i] = max(dp[i], dp[e] + e - s + t)
        return dp[0]
```

**Solution 2: (DP Top-Down)**
```
Runtime: 2320 ms
Memory Usage: 184.6 MB
```
```python
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        mp = {}
        for start, end, tip in rides: 
            mp.setdefault(start, []).append((end, tip))
        
        @cache
        def fn(x): 
            """Return max earning at x."""
            if x == n: return 0 
            ans = fn(x+1)
            for xx, tip in mp.get(x, []): 
                ans = max(ans, xx - x + tip + fn(xx))
            return ans 
        
        return fn(1)
```

**Solution 3: (DP Bottom-Up)**
```
Runtime: 492 ms
Memory Usage: 106.8 MB
```
```python
class Solution {
public:
    long long maxTaxiEarnings(int n, vector<vector<int>>& rides) {
        sort(rides.begin(), rides.end());
        vector<long long> dp(n+1);
        int j = 0;
        for(int i = 1; i <= n; ++i) {
            dp[i] = max(dp[i], dp[i - 1]);
            while (j < rides.size() && rides[j][0] == i)
                dp[rides[j++][1]] = max(dp[rides[j][1]], dp[i] + rides[j][1] - rides[j][0] + rides[j][2]);
        }
        return dp[n];
    }
};
```
