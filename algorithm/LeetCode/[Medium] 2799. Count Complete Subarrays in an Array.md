2799. Count Complete Subarrays in an Array

You are given an array `nums` consisting of positive integers.

We call a subarray of an array **complete** if the following condition is satisfied:

* The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.

Return the number of **complete** subarrays.

A subarray is a contiguous non-empty part of an array.

 

**Example 1:**
```
Input: nums = [1,3,1,2,2]
Output: 4
Explanation: The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].
```

**Example 2:**
```
Input: nums = [5,5,5,5]
Output: 10
Explanation: The array consists only of the integer 5, so any subarray is complete. The number of subarrays that we can choose is 10.
```

**Constraints:**

* `1 <= nums.length <= 1000`
* `1 <= nums[i] <= 2000`

# Submissions
---
**Solution 1: (Sliding Window, left index as count)**
```
Runtime: 106 ms
Memory: 16.6 MB
```
```python
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n, k = len(nums), len(set(nums))
        res = i = 0
        count = Counter()
        for j in range(n):
            count[nums[j]] += 1
            while len(count) == k:
                count[nums[i]] -= 1
                if count[nums[i]] == 0:
                    del count[nums[i]]
                i += 1
            res += i
        return res
```

**Solution 2: (Sliding Window)**

    1  3  1  2  2
    ^i       ^j
          ^i    ^j
    ----------
    -------------
       -------
       ----------


    5  5  5  5
    ^ij
       ^ij


```
Runtime: 15 ms, Beats 80.59%
Memory: 41.80 MB, Beats 71.22%
```
```c++
class Solution {
public:
    int countCompleteSubarrays(vector<int>& nums) {
        int n = nums.size(), i = 0, j, a = unordered_set(nums.begin(), nums.end()).size(), ans = 0;
        unordered_map<int,int> cnt;
        for (j = 0; j < n; j ++) {
            cnt[nums[j]] += 1;
            while (cnt.size() == a) {
                ans += n - j;
                cnt[nums[i]] -= 1;
                if (cnt[nums[i]] == 0) {
                    cnt.erase(nums[i]);
                }
                i += 1;
            }
        }
        return ans;
    }
};
```
