3152. Special Array II

An array is considered **special** if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integer `nums` and a 2D integer matrix `queries`, where for `queries[i] = [fromi, toi]` your task is to check that **subarray** `nums[fromi..toi]` is **special** or not.

Return an array of booleans `answer` such that `answer[i]` is `true` if `nums[fromi..toi]` is special.

 

**Example 1:**
```
Input: nums = [3,4,1,2,6], queries = [[0,4]]

Output: [false]

Explanation:

The subarray is [3,4,1,2,6]. 2 and 6 are both even.
```

**Example 2:**
```
Input: nums = [4,3,1,6], queries = [[0,2],[2,3]]

Output: [false,true]

Explanation:

The subarray is [4,3,1]. 3 and 1 are both odd. So the answer to this query is false.
The subarray is [1,6]. There is only one pair: (1,6) and it contains numbers with different parity. So the answer to this query is true.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^5`
* `1 <= queries.length <= 10^5`
* `queries[i].length == 2`
* `0 <= queries[i][0] <= queries[i][1] <= nums.length - 1`

# Submissions
---
**Solution 1: (Prefix Sum)**
```
Runtime: 181 ms
Memory: 125.76 MB
```
```c++
class Solution {
public:
    vector<bool> isArraySpecial(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size(), pre = -1;
        vector<int> dp(n);
        dp[0] = -1;
        for (int i = 1; i < n; i ++) {
            if (nums[i]%2 == nums[i-1]%2) {
                pre = i-1;
            }
            dp[i] = pre;
        }
        vector<bool> ans;
        for (int i = 0; i < queries.size(); i ++) {
            ans.push_back(queries[i][0] > dp[queries[i][1]]);
        }
        return ans;
    }
};
```
