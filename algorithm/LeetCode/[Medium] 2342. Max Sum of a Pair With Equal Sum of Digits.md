2342. Max Sum of a Pair With Equal Sum of Digits

You are given a **0-indexed** array `nums` consisting of **positive** integers. You can choose two indices `i` and `j`, such that `i != j`, and the sum of digits of the number `nums[i]` is equal to that of `nums[j]`.

Return the **maximum** value of `nums[i] + nums[j]` that you can obtain over all possible indices `i` and `j` that satisfy the conditions.

 

**Example 1:**
```
Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.
```

**Example 2:**
```
Input: nums = [10,12,19,14]
Output: -1
Explanation: There are no two numbers that satisfy the conditions, so we return -1.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (Hash Table)**
```
Runtime: 2981 ms
Memory Usage: 29.3 MB
```
```python
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = {}
        res = -1
        for num in nums:
            s = sum([int(digit) for digit in str(num)])
            if s not in d:
                d[s] = num
            else:
                res = max(res, d[s] + num)
                d[s] = max(d[s], num)
        return res 
```

**Solution 2: (Hash Table)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 63.66 MB, Beats 95.95%
```
```c++
class Solution {
public:
    int maximumSum(vector<int>& nums) {
        int dp[90] = {0}, cur, r, ans = -1;
        for (auto num: nums) {
            cur = 0;
            r = num;
            while (r) {
                cur += r%10;
                r /= 10;
            }
            if (dp[cur]) {
                ans = max(ans, dp[cur] + num);
            }
            dp[cur] = max(dp[cur], num);
        }
        return ans;
    }
};
```
