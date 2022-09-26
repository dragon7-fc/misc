2419. Longest Subarray With Maximum Bitwise AND

You are given an integer array `nums` of size `n`.

Consider a **non-empty** subarray from `nums` that has the **maximum** possible **bitwise AND**.

* In other words, let `k` be the maximum value of the bitwise AND of any subarray of `nums`. Then, only subarrays with a bitwise AND equal to `k` should be considered.

Return the length of the **longest** such subarray.

The bitwise AND of an array is the bitwise AND of all the numbers in it.

A **subarray** is a contiguous sequence of elements within an array.

 

**Example 1:**
```
Input: nums = [1,2,3,3,2,2]
Output: 2
Explanation:
The maximum possible bitwise AND of a subarray is 3.
The longest subarray with that value is [3,3], so we return 2.
```

**Example 2:**
```
Input: nums = [1,2,3,4]
Output: 1
Explanation:
The maximum possible bitwise AND of a subarray is 4.
The longest subarray with that value is [4], so we return 1.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^6`

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 2147 ms
Memory Usage: 28.2 MB
```
```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        MAX = max(nums) ### Find the largest number in nums.
        res = 0			 
        count = 0		### Used to count the length of the continues subarray that only contains MAX
        for n in nums:
        	### If the current number is MAX, increase count
            if n==MAX:
                count +=1
            ### Otherwise, reset count.
            else:
                count = 0
            ### store the maximum count as result.
            res = max(res, count)
        return res
```

**Solution 2: (Greedy)**
```
Runtime: 461 ms
Memory Usage: 82.3 MB
```
```c++
class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int N = nums.size();
        int maxEle = *max_element(nums.begin(), nums.end());
        int subarrayLen = 0, ans = 1;
        
        for(int i = 0; i < N; i++) {
            if (nums[i] == maxEle) {
                subarrayLen++;
                ans = max(ans, subarrayLen);
            } else {
                subarrayLen = 0;
            }
        }
        return ans;
    }
};
```
