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

**Solution 2: (Sliding Window, counter)**
```
Runtime: 126 ms
Memory: 95.14 MB
```
```c++
class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        unordered_map<int,int> cnt;
        long long cur = 0, ans = 0;
        for (int i = 0; i < nums.size(); i ++) {
            cur += nums[i];
            cnt[nums[i]] += 1;
            if (i >= k-1) {
                if (cnt.size() == k) {
                    ans = max(ans, cur);
                }
                cur -= nums[i-k+1];
                cnt[nums[i-k+1]] -= 1;
                if (!cnt[nums[i-k+1]]) {
                    cnt.erase(nums[i-k+1]);
                }
            }
        }
        return ans;
    }
};
```

**Solution 3: (Sliding Window)**
```
Runtime: 92 ms
Memory: 98.23 MB
```
```c++
class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        long long ans = 0;
        long long currentSum = 0;
        int begin = 0;
        int end = 0;

        unordered_map<int, int> numToIndex;

        while (end < nums.size()) {
            int currNum = nums[end];
            int lastOccurrence =
                (numToIndex.count(currNum) ? numToIndex[currNum] : -1);

            // if current window already has number or if window is too big,
            // adjust window
            while (begin <= lastOccurrence || end - begin + 1 > k) {
                currentSum -= nums[begin];
                begin++;
            }
            numToIndex[currNum] = end;
            currentSum += nums[end];
            if (end - begin + 1 == k) {
                ans = max(ans, currentSum);
            }
            end++;
        }
        return ans;
    }
};
```


**Solution 4: (Sliding Windows, last pointer)**
```
Runtime: 16 ms
Memory: 109.62 MB
```
```c++
class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        vector<int> dp(100001, -1);
        int i = -1;
        long long cur = 0, ans = 0;
        for (int j = 0; j < nums.size(); j ++) {
            cur += nums[j];
            while (i+1 <= dp[nums[j]]) {
                i += 1;
                cur -= nums[i];
            }
            if (j-i >= k) {
                ans = max(ans, cur);
                i += 1;
                cur -= nums[i];
            }
            dp[nums[j]] = j;
        }
        return ans;
    }
};
```

**Solution 5: (Sliding Windows, last pointer)**
```
Runtime: 18 ms
Memory: 109.66 MB
```
```c++
class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        vector<int> dp(100001, -1);
        int i = -1;
        long long cur = 0, ans = 0;
        for (int j = 0; j < nums.size(); j ++) {
            cur += nums[j];
            if (j >= k) {
                cur -= nums[j-k];
            }
            i = max(i, dp[nums[j]]);
            if (j-i >= k) {
                ans = max(ans, cur);
            }
            dp[nums[j]] = j;
        }
        return ans;
    }
};`
``
