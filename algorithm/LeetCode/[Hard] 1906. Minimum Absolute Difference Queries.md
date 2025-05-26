1906. Minimum Absolute Difference Queries

The **minimum absolute difference** of an array `a` is defined as the minimum value of `|a[i] - a[j]|`, where `0 <= i < j < a.length` and `a[i] != a[j]`. If all elements of `a` are the **same**, the minimum absolute difference is `-1`.

* For example, the minimum absolute difference of the array `[5,2,3,7,2]` is `|2 - 3| = 1`. Note that it is not `0` because `a[i]` and `a[j]` must be different.

You are given an integer array `nums` and the array `queries` where `queries[i] = [li, ri]`. For each query `i`, compute the **minimum absolute difference** of the subarray `nums[li...ri]` containing the elements of `nums` between the **0-based** indices `li` and `ri` (**inclusive**).

Return an **array** `ans` where `ans[i]` is the answer to the `i`th query.

A **subarray** is a contiguous sequence of elements in an array.

The value of `|x|` is defined as:

* `x` if `x >= 0`.
* `-x` if `x < 0`.
 

**Example 1:**
```
Input: nums = [1,3,4,8], queries = [[0,1],[1,2],[2,3],[0,3]]
Output: [2,1,4,1]
Explanation: The queries are processed as follows:
- queries[0] = [0,1]: The subarray is [1,3] and the minimum absolute difference is |1-3| = 2.
- queries[1] = [1,2]: The subarray is [3,4] and the minimum absolute difference is |3-4| = 1.
- queries[2] = [2,3]: The subarray is [4,8] and the minimum absolute difference is |4-8| = 4.
- queries[3] = [0,3]: The subarray is [1,3,4,8] and the minimum absolute difference is |3-4| = 1.
```

**Example 2:**
```
Input: nums = [4,5,2,2,7,10], queries = [[2,3],[0,2],[0,5],[3,5]]
Output: [-1,1,1,3]
Explanation: The queries are processed as follows:
- queries[0] = [2,3]: The subarray is [2,2] and the minimum absolute difference is -1 because all the
  elements are the same.
- queries[1] = [0,2]: The subarray is [4,5,2] and the minimum absolute difference is |4-5| = 1.
- queries[2] = [0,5]: The subarray is [4,5,2,2,7,10] and the minimum absolute difference is |4-5| = 1.
- queries[3] = [3,5]: The subarray is [2,7,10] and the minimum absolute difference is |7-10| = 3.
```

**Constraints:**

* `2 <= nums.length <= 10^5`
* `1 <= nums[i] <= 100`
* `1 <= queries.length <= 2 * 10^4`
* `0 <= li < ri < nums.length`

# Submissions
---
**Solution 1: (Prefix sum)**
```
Runtime: 3072 ms
Memory Usage: 108.8 MB
```
```python
class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        N, ans, dp = max(nums), [], [[0]*(max(nums)+1)]
        
        for num in nums:
            t = dp[-1][:]
            t[num] += 1
            dp.append(t)

        for a, b in queries:
            diff = [i for x, y, i in zip(dp[b+1], dp[a], range(N+1)) if y != x]
            ans.append(min([b-a for a,b in zip(diff, diff[1:])] or [-1]))
        
        return ans
```

**Solution 2: (Prefix sum)**
```
Runtime: 300 ms
Memory: 129.00 MB
```
```c++
class Solution {
    int cnt[100001][101] = {};
public:
    vector<int> minDifference(vector<int>& nums, vector<vector<int>>& queries) {
        vector<int> res;
        for (int i = 0; i < nums.size(); ++i)
            for (int j = 1; j <= 100; ++j)
                cnt[i + 1][j] = cnt[i][j] + (nums[i] == j);
        for (int i = 0; i < queries.size(); ++i) {
            int prev = 0, delta = INT_MAX;
            for (int j = 1; j <= 100; ++j)
                if (cnt[queries[i][1] + 1][j] - cnt[queries[i][0]][j]) {
                    delta = min(delta, prev == 0 ? INT_MAX : j - prev);
                    prev = j;
                }
            res.push_back(delta == INT_MAX ? -1 : delta);
        }
        return res;
    }
};
```

**Solution 2: (Binary Search)**

    nums = [4,5,2,2,7,10], queries = [[2,3],[0,2],[0,5],[3,5]]


    3
    2 0 1 4  5
   ------------
    2 4 5 7 10

```
Runtime: 359 ms
Memory: 91.03 MB
```
```c++
class Solution {
public:
    vector<int> minDifference(vector<int>& nums, vector<vector<int>>& queries) {
        vector<int> res, idx[101];
        for (int i = 0; i < nums.size(); ++i)
            idx[nums[i]].push_back(i);
        for (int i = 0; i < queries.size(); ++i) {
            int prev = 0, delta = INT_MAX;
            for (int j = 1; j <= 100; ++j) {
                auto it = lower_bound(begin(idx[j]), end(idx[j]), queries[i][0]);
                if (it != end(idx[j]) && *it <= queries[i][1]) {
                    delta = min(delta, prev == 0 ? INT_MAX : j - prev);
                    prev = j;
                }
            }
            res.push_back(delta == INT_MAX ? -1 : delta);
        }
        return res;
    }
};
```
