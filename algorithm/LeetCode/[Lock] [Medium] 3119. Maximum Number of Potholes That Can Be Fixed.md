3119. Maximum Number of Potholes That Can Be Fixed

You are given a string `road`, consisting only of characters `"x"` and `"."`, where each `"x"` denotes a pothole and each `"."` denotes a smooth road, and an integer `budget`.

In one repair operation, you can repair n **consecutive** potholes for a price of `n + 1`.

Return the **maximum** number of potholes that can be fixed such that the sum of the prices of all of the fixes doesn't go over the given `budget`.

 

**Example 1:**
```
Input: road = "..", budget = 5

Output: 0

Explanation:

There are no potholes to be fixed.
```

**Example 2:**
```
Input: road = "..xxxxx", budget = 4

Output: 3

Explanation:

We fix the first three potholes (they are consecutive). The budget needed for this task is 3 + 1 = 4.
```

**Example 3:**
```
Input: road = "x.x.xxx...x", budget = 14

Output: 6

Explanation:

We can fix all the potholes. The total cost would be (1 + 1) + (1 + 1) + (3 + 1) + (1 + 1) = 10 which is within our budget of 14.
```
 

**Constraints:**

* `1 <= road.length <= 105`
* `1 <= budget <= 105 + 1`
* `road` consists only of characters `'.'` and `'x'`.

# Submissions
---
**Solution 1: (Greedy, Sort)**
```
Runtime: 116 ms
Memory: 44.11 MB
```
```c++
class Solution {
public:
    int maxPotholes(string road, int budget) {
        int n = road.size(), i = 0, k, ans;
        vector<int> dp;
        while (i < n) {
            if (road[i] == '.') {
                i += 1;
                continue;
            }
            k = 1;
            while ((i+k) < n && road[i+k] == 'x') {
                k += 1;
            }
            dp.push_back(k+1);
            i += k;
        }
        sort(dp.begin(), dp.end(), [](auto a, auto b){return a > b;});
        i = 0, ans = 0;
        while (i < dp.size()) {
            if (budget <= dp[i]) {
                ans += budget-1;
                break;
            }
            budget -= dp[i];
            ans += dp[i]-1;
            i += 1;
        }
        return ans;
    }
};
```
