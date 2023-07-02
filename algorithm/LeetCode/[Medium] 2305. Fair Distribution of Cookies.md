2305. Fair Distribution of Cookies

You are given an integer array `cookies`, where `cookies[i]` denotes the number of cookies in the `i`th bag. You are also given an integer `k` that denotes the number of children to distribute all the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.

The **unfairness** of a distribution is defined as the **maximum total** cookies obtained by a single child in the distribution.

Return the **minimum** unfairness of all distributions.

 

**Example 1:**
```
Input: cookies = [8,15,10,20,8], k = 2
Output: 31
Explanation: One optimal distribution is [8,15,8] and [10,20]
- The 1st child receives [8,15,8] which has a total of 8 + 15 + 8 = 31 cookies.
- The 2nd child receives [10,20] which has a total of 10 + 20 = 30 cookies.
The unfairness of the distribution is max(31,30) = 31.
It can be shown that there is no distribution with an unfairness less than 31.
```

**Example 2:**
```
Input: cookies = [6,1,3,2,2,4,1,2], k = 3
Output: 7
Explanation: One optimal distribution is [6,1], [3,2,2], and [4,1,2]
- The 1st child receives [6,1] which has a total of 6 + 1 = 7 cookies.
- The 2nd child receives [3,2,2] which has a total of 3 + 2 + 2 = 7 cookies.
- The 3rd child receives [4,1,2] which has a total of 4 + 1 + 2 = 7 cookies.
The unfairness of the distribution is max(7,7,7) = 7.
It can be shown that there is no distribution with an unfairness less than 7.
```

**Constraints:**

* `2 <= cookies.length <= 8`
* `1 <= cookies[i] <= 10^5`
* `2 <= k <= cookies.length`

# Submissions
---
**SOlution 1: (Backtracking)**
```
Runtime: 47 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = float('inf')
        fair = [0]*k
        def rec(i):
            nonlocal ans,fair
            if i == len(cookies):
                ans = min(ans,max(fair))
                return
			# Bounding condition to stop a branch if unfairness already exceeds current optimal soltution
            if ans <= max(fair):
                return
            for j in range(k):
                fair[j] += cookies[i]
                rec(i+1)
                fair[j] -= cookies[i]
        rec(0)
        return ans
```

**SOlution 2: (Backtracking, multi-knapsack problem, NP-complete)**
```
Runtime: 2316 ms
Memory: 7 MB
```
```c++
class Solution {
    void bt(int i, vector<int> &cookies, vector<int> &g, int k, int &ans){
        if (i == cookies.size()){
            int mx = INT_MIN;
            for(int j = 0; j < k; j++){
                mx = max(mx, g[j]);
            }
            ans = min(ans, mx);
            return;
        }
        for (int j = 0; j < k; j++){
            g[j] += cookies[i];
            bt(i+1, cookies, g, k, ans);
            g[j] -= cookies[i];
        }
    }
public:
    int distributeCookies(vector<int>& cookies, int k) {
        int n = cookies.size(), ans = INT_MAX;
        vector<int> g(k);
        bt(0, cookies, g, k, ans);
        return ans;
    }
};
```

**Solution 3: (DP Top-Down, DFS with Mask)**
```
Runtime: 7 ms
Memory: 6.8 MB
```
```c++
class Solution {
    int dp[7][255] = {};
    int mask_sum(vector<int>& cookies, int mask) {
        int sum = 0;
        for (int j = 0; j < cookies.size(); ++j)
            sum += (mask & (1 << j)) ? cookies[j] : 0;
        return sum;    
    }
public:
    int distributeCookies(vector<int>& cookies, int k, int i = 0, int mask = 0) {
        int lim = (1 << cookies.size()) - 1;
        if (i == k - 1)
            return mask_sum(cookies, lim - mask);
        if (dp[i][mask] == 0) {
            dp[i][mask] = INT_MAX;
            for (int mask_i = 1; mask_i < lim; ++mask_i)
                if ((mask_i & mask) == 0 && __builtin_popcount(lim - mask_i - mask) >= k - i - 1)
                    dp[i][mask] = min(dp[i][mask], 
                        max(distributeCookies(cookies, k, i + 1, mask + mask_i), mask_sum(cookies, mask_i)));
        }
        return dp[i][mask];
    }
};
```
