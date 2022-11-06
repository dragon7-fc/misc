2461. Maximum Sum of Distinct Subarrays With Length K

You are given an integer array `nums` and an integer `k`. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

* The length of the subarray is `k`, and
* All the elements of the subarray are distinct.

Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return `0`.

A **subarray** is a contiguous non-empty sequence of elements within an array.

 

**Example 1:**
```
Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions
```

**Example 2:**
```
Input: nums = [4,4,4], k = 3
Output: 0
Explanation: The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions.
```

**Constraints:**

* `1 <= k <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^5`

# Submissions
---
**Solution 1: (last position)**
```
Runtime: 2958 ms
Memory: 29 MB
```
```python
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res, cur, pos, dup = 0, 0, [-1] * 100001, -1
        
        for i in range(0,len(nums)):
            cur += nums[i]                      # compute running sum for
            if i >= k: cur -= nums[i-k]         # the window of length k
            
            if i - pos[nums[i]] < k:            # update LAST seen duplicate 
                dup = max(dup, pos[nums[i]])    # number among last k numbers
            
            if i - dup >= k:                    # if no duplicates were found
                res = max(res, cur)             # update max window sum

            pos[nums[i]] = i

        return res
```

**Solution 2: (last position)**
```
Runtime: 155 ms
Memory: 136.6 MB
```
```c++
class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        long long res = 0, cur = 0, dup = -1;
        vector<long long> pos(100001,-1);
        
        for (int i = 0; i < nums.size(); ++i)
        {
            cur += nums[i];
            if (i >= k) cur -= nums[i-k];
            
            if (i - pos[nums[i]] < k)
                dup = max(dup, pos[nums[i]]);
            
            if (i - dup >= k) res = max(res, cur);
            
            pos[nums[i]] = i;
        }
        
        return res;
    }
};
```
