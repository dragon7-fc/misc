1248. Count Number of Nice Subarrays

Given an array of integers `nums` and an integer `k`. A subarray is called nice if there are `k` odd numbers on it.

Return the number of nice sub-arrays.

 

**Example 1:**
```
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
```

**Example 2:**
```
Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.
```

**Example 3:**
```
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
```

**Constraints:**

* `1 <= nums.length <= 50000`
* `1 <= nums[i] <= 10^5`
* `1 <= k <= nums.length`

# Submissions
---
**Solution 1: (Two Pointers)**
```
Runtime: 844 ms
Memory Usage: 19.4 MB
```
```python
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        arr = [-1] + [i for i, num in enumerate(nums) if num & 1] + [len(nums)]
        return sum([(j - i) * (l - k) for i, j, k, l in zip(
            arr,
            arr[1:],
            arr[k:],
            arr[k+1:]
        )])
```

**Solution 1: (Prefix Sum)**
```
Runtime: 80 ms
Memory: 74.15 MB
```
```c++
class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int n = nums.size(), ans = 0;
        vector<int> dp;
        dp.push_back(-1);
        for (int i = 0; i < n; i ++) {
            if (nums[i]%2) {
                dp.push_back(i);
            }
        }
        dp.push_back(n);
        for (int i = k; i < dp.size()-1; i ++) {
            ans += (dp[i+1]-dp[i])*(dp[i-k+1]-dp[i-k]);
        }
        return ans;
    }
};
```
