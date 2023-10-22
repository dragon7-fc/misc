2393. Count Strictly Increasing Subarrays

You are given an array `nums` consisting of positive integers.

Return the number of **subarrays** of `nums` that are in **strictly increasing** order.

A **subarray** is a contiguous part of an array.

 

**Example 1:**
```
Input: nums = [1,3,5,4,4,6]
Output: 10
Explanation: The strictly increasing subarrays are the following:
- Subarrays of length 1: [1], [3], [5], [4], [4], [6].
- Subarrays of length 2: [1,3], [3,5], [4,6].
- Subarrays of length 3: [1,3,5].
The total number of subarrays is 6 + 3 + 1 = 10.
```

**Example 2:**
```
Input: nums = [1,2,3,4,5]
Output: 15
Explanation: Every subarray is strictly increasing. There are 15 possible subarrays that we can take.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^6`

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 861 ms
Memory: 29 MB
```
```python
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ans = cur = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cur += 1
            else:
                cur = 1
            ans += cur
        return ans
```

**Solution 2: (Two Pointers)**
```
Runtime: 114 ms
Memory: 76.1 MB
```
```c++
class Solution {
public:
    long long countSubarrays(vector<int>& nums) {
        long long res = 0;
        for (int i = 1, j = 0; i < nums.size(); ++i) {
            if (nums[i - 1] >= nums[i])
                j = i;
            res += i - j;
        }
        return res + nums.size();
    }
};
```
