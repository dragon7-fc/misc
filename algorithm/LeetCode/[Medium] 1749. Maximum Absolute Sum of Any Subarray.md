1749. Maximum Absolute Sum of Any Subarray

You are given an integer array `nums`. The absolute sum of a subarray `[numsl, numsl+1, ..., numsr-1, numsr]` is `abs(numsl + numsl+1 + ... + numsr-1 + numsr)`.

Return the maximum absolute sum of any (possibly empty) subarray of `nums`.

Note that `abs(x)` is defined as follows:

* If `x` is a negative integer, then `abs(x) = -x`.
* If `x` is a non-negative integer, then `abs(x) = x`.
 

**Example 1:**
```
Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.
```

**Example 2:**
```
Input: nums = [2,-5,1,-4,3,-2]
Output: 8
Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `-10^4 <= nums[i] <= 10^4`

# Submissions
---
**Solution 1: (Prefix Sum)**

**Explanation**

Just find the maximum prefix sum and the minimum prefix sum.
return max - min.

Proof as homework,
Please think at least 10 minutes before you need a proof.


**Proof**

abs subarray sum
= one prefix sum - the other prefix sum
<= maximum prefix sum - minimum prefix sum


**Complexity**

* Time O(n)
* Space O(1)

```
Runtime: 364 ms
Memory Usage: 28.5 MB
```
```python
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        return max(accumulate(nums, initial=0)) - min(accumulate(nums, initial=0))
```

**Solution 2: (Prefix Sum)**

         1,-3, 2, 3,-4
                ^^^^
cur 0    1 -2  0  3 -1
min      0  0 -2 -2 -2
max      0  1  1  1  3
ans      1  3  3  5  5

      2,-5, 1,-4, 3,-2
         ^^^^^^^
pre 0 2 -3 -2 -6 -3 -5
min   0  0 -3 -3 -6 -6
max   0  2  2  2  2  2
ans   2  5  5  8  8  8

```
Runtime: 0 ms, Beats  100.00%
Memory: 45.21 MB, Beats 20.65%
```
```c++
class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
        int n = nums.size(), i, cur = 0, mn = 0, mx = 0, ans = INT_MIN;
        for (i = 0; i < n; i ++) {
            cur += nums[i];
            if (cur >= 0) {
                ans = max(ans, cur - mn);
            } else if (cur < 0) {
                ans = max(ans, mx - cur);
            }
            mn = min(mn, cur);
            mx = max(mx, cur);
        }
        return ans;
    }
};
```

**Solution 3: (Prefix Sum - Shorter)**

        2,-5, 1,-4, 3,-2
pre  0  2 -3 -2 -6 -3 -1
min  0  0 -3 -3 -6 -6 -6
max  0  2  2  2  2  2  2

```
Runtime: 3 ms, Beats 24.38%
Memory: 45.00 MB, Beats 78.26%
```
```c++
class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
        int minPrefixSum = 0, maxPrefixSum = 0;

        int prefixSum = 0;
        for (int i = 0; i < nums.size(); i++) {
            prefixSum += nums[i];

            minPrefixSum = min(minPrefixSum, prefixSum);
            maxPrefixSum = max(maxPrefixSum, prefixSum);
        }

        return maxPrefixSum - minPrefixSum;
    }
};
```
