3578. Count Partitions With Max-Min Difference at Most K

You are given an integer array `nums` and an integer `k`. Your task is to partition `nums` into one or more non-empty contiguous segments such that in each segment, the difference between its **maximum** and **minimum** elements is **at most** `k`.

Return the total number of ways to partition `nums` under this condition.

Since the answer may be too large, return it modulo `10^9 + 7`.

 

**Example 1:**
```
Input: nums = [9,4,1,3,7], k = 4

Output: 6

Explanation:

There are 6 valid partitions where the difference between the maximum and minimum elements in each segment is at most k = 4:

[[9], [4], [1], [3], [7]]
[[9], [4], [1], [3, 7]]
[[9], [4], [1, 3], [7]]
[[9], [4, 1], [3], [7]]
[[9], [4, 1], [3, 7]]
[[9], [4, 1, 3], [7]]
```

**Example 2:**
```
Input: nums = [3,3,4], k = 0

Output: 2

Explanation:

There are 2 valid partitions that satisfy the given conditions:

[[3], [3], [4]]
[[3, 3], [4]]
```

**Constraints:**

* `2 <= nums.length <= 5 * 10^4`
* `1 <= nums[i] <= 10^9`
* `0 <= k <= 10^9`

# Submissions
---
**Solution 1: (multiset, DP)**

                     vi
     9   4   1   3   7
ws 0 1   2   2   4   8
         1   
ms   9   49  14  134 1347
         x           x x
dp   1   1   1   2   4    6
                 ^j

```
Runtime: 278 ms, Beats 50.00%
Memory: 211.82 MB, Beats 25.00%
```
```c++
class Solution {
    int dp[50001] = {1}, mod = 1000000007;
public:
    int countPartitions(vector<int>& nums, int k) {
        long long window_sum = 0;
        multiset<int> ms;
        for (int i = 0, j = 0; i < nums.size(); ++i) {
            window_sum = (window_sum + dp[i]) % mod;
            ms.insert(nums[i]);
            while (*prev(end(ms)) - *begin(ms) > k) {
                window_sum = (mod + window_sum - dp[j]) % mod;
                ms.erase(ms.find(nums[j++]));
            }
            dp[i + 1] = window_sum;
        }
        return dp[nums.size()];
    }
};
```

**Solution 1: (Deque, DP)**

                    vi
        9   4   1   3   7
                        ^j
dp      1   1   1   2   4   6
minq    9   94  41  413 437
            x        x  xx
maxq    9   4   1   13  137
acc  1  1   1   2   4   8

```
Runtime: 58 ms, Beats 87.50%
Memory: 145.92 MB, Beats 87.50%
```
```c++
class Solution {
public:
    int countPartitions(vector<int>& nums, int k) {
        int n = nums.size(), mod = 1e9 + 7, acc = 1;
        vector<int> dp(n + 1, 0);
        dp[0] = 1;

        deque<int> minq, maxq;
        for (int i = 0, j = 0; j < n; ++j) {
            while (!maxq.empty() && nums[j] > nums[maxq.back()])
                maxq.pop_back();
            maxq.push_back(j);
            while (!minq.empty() && nums[j] < nums[minq.back()])
                minq.pop_back();
            minq.push_back(j);
            while (nums[maxq.front()] - nums[minq.front()] > k) {
                acc = (acc - dp[i++] + mod) % mod;
                if (minq.front() < i)
                    minq.pop_front();
                if (maxq.front() < i)
                    maxq.pop_front();
            }

            dp[j + 1] = acc;
            acc = (acc + dp[j + 1]) % mod;
        }
        return dp[n];
    }
};
```
