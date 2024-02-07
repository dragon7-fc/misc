2830. Maximize the Profit as the Salesman

You are given an integer `n` representing the number of houses on a number line, numbered from `0` to `n - 1`.

Additionally, you are given a 2D integer array `offers` where `offers[i] = [starti, endi, goldi]`, indicating that `i`th buyer wants to buy all the houses from `starti` to `endi` for `goldi` amount of gold.

As a salesman, your goal is to maximize your earnings by strategically selecting and selling houses to buyers.

Return the maximum amount of gold you can earn.

**Note** that different buyers can't buy the same house, and some houses may remain unsold.

 

**Example 1:**
```
Input: n = 5, offers = [[0,0,1],[0,2,2],[1,3,2]]
Output: 3
Explanation: There are 5 houses numbered from 0 to 4 and there are 3 purchase offers.
We sell houses in the range [0,0] to 1st buyer for 1 gold and houses in the range [1,3] to 3rd buyer for 2 golds.
It can be proven that 3 is the maximum amount of gold we can achieve.
```

**Example 2:**
```
Input: n = 5, offers = [[0,0,1],[0,2,10],[1,3,2]]
Output: 10
Explanation: There are 5 houses numbered from 0 to 4 and there are 3 purchase offers.
We sell houses in the range [0,2] to 2nd buyer for 10 golds.
It can be proven that 10 is the maximum amount of gold we can achieve.
```

**Constraints:**

* `1 <= n <= 10^5`
* `1 <= offers.length <= 10^5`
* `Offers[i].length == 3`
* `0 <= starti <= endi <= n - 1`
* `1 <= goldi <= 10^3`

**Solution 1: (DP Bottom-Up)**
```
Runtime: 374 ms
Memory: 139.5 MB
```
```c++
class Solution {
public:
    int maximizeTheProfit(int n, vector<vector<int>>& offers) {
        int dp[100002] = {};
        unordered_map<int, vector<pair<int, int>>> m;
        for (const auto &offer : offers)
            m[offer[1]].push_back({offer[0], offer[2]});
        for (int k = 0; k < n; ++k) {
            dp[k + 1] = dp[k];
            if (m.count(k))
                for (auto [start, gold] : m[k])
                    dp[k + 1] = max(dp[k + 1], dp[start] + gold);
        }
        return dp[n];
    }
};
```

**Solution 2: (Binary Search)**
```
Runtime: 316 ms
Memory: 113.26 MB
```
```c++
class Solution {
    int helper(vector<int>& dp, vector<vector<int>>& v, int n) {
        vector<int> s, e; 
        for (auto i : v) {
            s.push_back(i[0]);
            e.push_back(i[1]);
        }

        for (int i = v.size() - 1; i >= 0; i--) {
            int check = upper_bound(s.begin(), s.end(), e[i]) - s.begin();
            dp[i] = max(v[i][2] + dp[check], dp[i + 1]);
        }

        return (*max_element(dp.begin(), dp.end()));
    }
public:
    int maximizeTheProfit(int n, vector<vector<int>>& offers) {
        vector<int> dp(offers.size() + 1, 0);
        sort(offers.begin(), offers.end());
        return helper(dp, offers, n);
    }
};
```
