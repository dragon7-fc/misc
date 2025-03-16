2560. House Robber IV

There are several consecutive houses along a street, each of which has some money inside. There is also a robber, who wants to steal money from the homes, but he **refuses to steal from adjacent homes**.

The **capability** of the robber is the maximum amount of money he steals from one house of all the houses he robbed.

You are given an integer array `nums` representing how much money is stashed in each house. More formally, the `i`th house from the left has `nums[i]` dollars.

You are also given an integer `k`, representing the minimum number of houses the robber will steal from. It is always possible to steal at least `k` houses.

Return the **minimum** capability of the robber out of all the possible ways to steal at least `k` houses.

 

**Example 1:**
```
Input: nums = [2,3,5,9], k = 2
Output: 5
Explanation: 
There are three ways to rob at least 2 houses:
- Rob the houses at indices 0 and 2. Capability is max(nums[0], nums[2]) = 5.
- Rob the houses at indices 0 and 3. Capability is max(nums[0], nums[3]) = 9.
- Rob the houses at indices 1 and 3. Capability is max(nums[1], nums[3]) = 9.
Therefore, we return min(5, 9, 9) = 5.
```

**Example 2:**
```
Input: nums = [2,7,9,3,1], k = 2
Output: 2
Explanation: There are 7 ways to rob the houses. The way which leads to minimum capability is to rob the house at index 0 and 4. Return max(nums[0], nums[4]) = 2.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^9`
* `1 <= k <= (nums.length + 1)/2`

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 856 ms
Memory: 24.9 MB
```
```python
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        l, r = min(nums), max(nums)
        while l < r:
            m = (l + r) // 2
            last = take = 0
            for a in nums:
                if last:
                    last = 0
                    continue
                if a <= m:
                    take += 1
                    last = 1
            if take >= k:
                r = m
            else:
                l = m + 1
        return l
```

**Solution 2: (Binary Search, search on value, DP Bottom-Up)**

    dp[i+1] = max(dp[i], dp[i-1] + (nums[i] < a))

```
Runtime: 9 ms, Beats 99.19%
Memory: 60.81 MB Beats 67.69%
```
```c++
class Solution {
    bool check(int a, vector<int> &nums, int k) {
        int n = nums.size(), i, cur, pre, pre2 = 0;
        pre = (nums[0] <= a);
        for (i = 1; i < n; i ++) {
            cur = max(pre, pre2 + (nums[i] <= a));
            pre2 = pre;
            pre = cur;
        }
        return pre >= k;
    }
public:
    int minCapability(vector<int>& nums, int k) {
        int left = 1, right = *max_element(nums.begin(), nums.end()), mid, ans;
        while (left <= right) {
            mid = left + (right - left)/2;
            if (!check(mid, nums, k)) {
                left = mid + 1;
            } else {
                ans = mid;
                right = mid - 1;
            }
        }
        return ans;
    }
};
```
