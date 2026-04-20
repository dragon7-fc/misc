3488. Closest Equal Element Queries

You are given a circular array `nums` and an array `queries`.

For each query `i`, you have to find the following:

The **minimum** distance between the element at index `queries[i]` and any other index `j` in the circular array, where `nums[j] == nums[queries[i]]`. If no such index exists, the answer for that query should be `-1`.

Return an array `answer` of the same size as `queries`, where `answer[i]` represents the result for query `i`.

 

**Example 1:**
```
Input: nums = [1,3,1,4,1,3,2], queries = [0,3,5]

Output: [2,-1,3]

Explanation:

Query 0: The element at queries[0] = 0 is nums[0] = 1. The nearest index with the same value is 2, and the distance between them is 2.
Query 1: The element at queries[1] = 3 is nums[3] = 4. No other index contains 4, so the result is -1.
Query 2: The element at queries[2] = 5 is nums[5] = 3. The nearest index with the same value is 1, and the distance between them is 3 (following the circular path: 5 -> 6 -> 0 -> 1).
```

**Example 2:**
```
Input: nums = [1,2,3,4], queries = [0,1,2,3]

Output: [-1,-1,-1,-1]

Explanation:

Each value in nums is unique, so no index shares the same value as the queried element. This results in -1 for all queries.
```
 

**Constraints:**

* `1 <= queries.length <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^6`
* `0 <= queries[i] < nums.length`

# Submissions
---
**Solution 1: (Hash Table, binary search)**
```
Runtime: 225 ms, Beats 51.24%
Memory: 214.04 MB, Beats 58.71%
```
```c++
class Solution {
public:
    vector<int> solveQueries(vector<int>& nums, vector<int>& queries) {
        int m = nums.size(), n = queries.size(), i, j, k;
        unordered_map<int, vector<int>> mp;
        for (i = 0; i < m; i ++) {
            mp[nums[i]].push_back(i);
        }
        vector<int> ans(n, -1);
        for (i = 0; i < n; i ++) {
            if (mp[nums[queries[i]]].size() > 1) {
                auto &dp = mp[nums[queries[i]]]; 
                k = dp.size();
                j = lower_bound(dp.begin(), dp.end(), queries[i]) - dp.begin();
                if (j) {
                    ans[i] = queries[i] - dp[j - 1];
                } else {
                    ans[i] = queries[i] + m - dp.back();
                }
                if (j != k-1) {
                    ans[i] = min(ans[i], dp[j + 1] - queries[i]);
                } else {
                    ans[i] = min(ans[i], m - queries[i] + dp[0]);
                }
            }
        }
        return ans;
    }
};
```

**Solution 2: (Hash Table, binary search, add satellite)**
```
Runtime: 319 ms, Beats 20.90%
Memory: 237.36 MB, Beats 11.94%
```
```c++
class Solution {
public:
    vector<int> solveQueries(vector<int>& nums, vector<int>& queries) {
        int m = nums.size(), n = queries.size(), i, j, k, x;
        unordered_map<int, vector<int>> mp;
        for (i = 0; i < m; i ++) {
            mp[nums[i]].push_back(i);
        }
        for (auto &[_, dp] : mp) {
            x = dp[0];
            dp.insert(dp.begin(), dp.back() - m);   // left satellite
            dp.push_back(x + m);    // right satellite
        }
        vector<int> ans(n, -1);
        for (i = 0; i < n; i ++) {
            if (mp[nums[queries[i]]].size() > 3) {
                auto &dp = mp[nums[queries[i]]]; 
                j = lower_bound(dp.begin(), dp.end(), queries[i]) - dp.begin();
                ans[i] = min(dp[j] - dp[j - 1], dp[j + 1] - dp[j]);
            }
        }
        return ans;
    }
};
```

**Solution 3: (Preprocessing Nearest Left and Right Positions + Hash Table, Prefix Sum)**

     -m       0       m-1 m        2*m-1
nums         [           ]
left -------------------->
right        <--------------------------

         -7 -6 -5 -4 -3 -2 -1  0  1  2  3  4  5  6  7  8  9 10 11 12 13
                       nums = [1, 3, 1, 4, 1, 3, 2],                         queries = [ 0, 3, 5]
mp        1  3  1  4  1  3  2                       1  3  1  4  1  3  2
left                          -3 -2  1 -4  2  1 -1
right                          2  5  4 10  7  8 13

ans                                                                                      2 -1  3                                                                                                           min(0-(-3), 2-0)
                                                                                               min(5-1, 8-5)
```
Runtime: 176 ms, Beats 87.06%
Memory: 199.38 MB, Beats 93.53%
```
```c++
class Solution {
public:
    vector<int> solveQueries(vector<int>& nums, vector<int>& queries) {
        int m = nums.size(), n = queries.size(), i, x;
        vector<int> left(m), right(m);
        unordered_map<int, int> mp;
        for (i = -m; i < m; i++) {
            if (i >= 0) {
                left[i] = mp[nums[i]];
            }
            mp[nums[(i + m) % m]] = i;
        }
        mp.clear();
        for (i = 2 * m - 1; i >= 0; i--) {
            if (i < m) {
                right[i] = mp[nums[i]];
            }
            mp[nums[i % m]] = i;
        }
        for (i = 0; i < n; i++) {
            x = queries[i];
            queries[i] =
                (x - left[x] == m) ? -1 : min(x - left[x], right[x] - x);
        }
        return queries;
    }
};
```
