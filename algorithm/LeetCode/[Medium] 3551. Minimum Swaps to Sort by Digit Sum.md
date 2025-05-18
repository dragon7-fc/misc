3551. Minimum Swaps to Sort by Digit Sum

You are given an array `nums` of **distinct** positive integers. You need to sort the array in **increasing** order based on the sum of the digits of each number. If two numbers have the same digit sum, the **smaller** number appears first in the sorted order.

Return the **minimum** number of swaps required to rearrange `nums` into this sorted order.

A **swap** is defined as exchanging the values at two distinct positions in the array.

 

Example 1:

Input: nums = [37,100]

**Output: 1**
```
Explanation:

Compute the digit sum for each integer: [3 + 7 = 10, 1 + 0 + 0 = 1] → [10, 1]
Sort the integers based on digit sum: [100, 37]. Swap 37 with 100 to obtain the sorted order.
Thus, the minimum number of swaps required to rearrange nums is 1.
```

**Example 2:**
```
Input: nums = [22,14,33,7]

Output: 0

Explanation:

Compute the digit sum for each integer: [2 + 2 = 4, 1 + 4 = 5, 3 + 3 = 6, 7 = 7] → [4, 5, 6, 7]
Sort the integers based on digit sum: [22, 14, 33, 7]. The array is already sorted.
Thus, the minimum number of swaps required to rearrange nums is 0.
```

**Example 3:**
```
Input: nums = [18,43,34,16]

Output: 2

Explanation:

Compute the digit sum for each integer: [1 + 8 = 9, 4 + 3 = 7, 3 + 4 = 7, 1 + 6 = 7] → [9, 7, 7, 7]
Sort the integers based on digit sum: [16, 34, 43, 18]. Swap 18 with 16, and swap 43 with 34 to obtain the sorted order.
Thus, the minimum number of swaps required to rearrange nums is 2.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^9`
* `nums` consists of **distinct** positive integers.

# Submissions
---
**Solution 1: (Sort, Hash Table)**
```
Runtime: 916 ms, Beats 12.48%
Memory: 218.52 MB, Beats 39.99%
```
```c++
class Solution {
public:
    int minSwaps(vector<int>& nums) {
        int n = nums.size(), i, ans = 0;
        unordered_map<int,int> m;
        vector<int> dp;
        for (i = 0; i < n; i ++) {
            dp.push_back(nums[i]);
            m[nums[i]] = i;
        }
        sort(dp.begin(), dp.end(), [](auto a, auto b){
            int pa = a, pb = b, da = 0, db = 0;
            while (a) {
                da += a%10;
                a /= 10;
            }
            while (b) {
                db += b%10;
                b /= 10;
            }
            if (da == db) {
                return pa < pb;
            } else {
                return da < db;
            }
        });
        for (i = 0; i < n; i ++) {
            if (m[dp[i]] != i) {
                swap(m[nums[i]], m[dp[i]]);
                swap(nums[m[nums[i]]], nums[m[dp[i]]]);
                ans += 1;
            }
        }
        return ans;
    }
};
```

**Solution 2: (Sort, cycle detection)**
```
Runtime: 610 ms, Beats 31.58%
Memory: 160.39 MB, Beats 80.55%
```
```c++
class Solution {
public:
    int minSwaps(vector<int>& nums) {
        int n = nums.size(), i, j, a, ans = 0;
        vector<pair<int,int>> dp;
        vector<int> visited(n);
        for (i = 0; i < n; i ++) {
            dp.push_back({nums[i], i});
        }
        sort(dp.begin(), dp.end(), [](auto pa, auto pb){
            int a = pa.first, b = pb.first, da = 0, db = 0;
            while (a) {
                da += a%10;
                a /= 10;
            }
            while (b) {
                db += b%10;
                b /= 10;
            }
            if (da == db) {
                return pa.first < pb.first;
            } else {
                return da < db;
            }
        });
        for (i = 0; i < n; i ++) {
            if (visited[i] || dp[i].second == i) {
                continue;
            }
            j = i;
            a = 0;
            while (!visited[j]) {
                visited[j] = 1;
                j = dp[j].second;
                a += 1;
            }
            ans += a-1;
        }
        return ans;

    }
};
```
