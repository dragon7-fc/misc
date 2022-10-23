2447. Number of Subarrays With GCD Equal to K

Given an integer array `nums` and an integer `k`, return the number of **subarrays** of `nums` where the greatest common divisor of the subarray's elements is `k`.

A **subarray** is a contiguous non-empty sequence of elements within an array.

The **greatest common divisor** of an array is the largest integer that evenly divides all the array elements.

 

**Example 1:**
```
Input: nums = [9,3,1,2,6,3], k = 3
Output: 4
Explanation: The subarrays of nums where 3 is the greatest common divisor of all the subarray's elements are:
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
```

**Example 2:**
```
Input: nums = [4], k = 7
Output: 0
Explanation: There are no subarrays of nums where 7 is the greatest common divisor of all the subarray's elements.
```

**Constraints:**

* `1 <= nums.length <= 1000`
* `1 <= nums[i], k <= 10^9`

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 932 ms
Memory: 14 MB
```
```python
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        # recursive function for finding gcd
        def gcd(a, b):
            if  b == 0: 
                return a
            return gcd(b , a % b)
            # Time complexity - O(log(min(a, b)) = O(log n)

        
        cnt = 0
        n = len(nums)
        
        for i in range(n):
            tmp_gcd = 0 # gcd of zero with any number is equal to the number itself
            
            for j in range(i,n):
                tmp_gcd = gcd(tmp_gcd, nums[j])
                
                

                if tmp_gcd == k:
                    cnt += 1
                elif tmp_gcd < k: # gcd cannot get bigger
                    break
        
        return cnt
```

**Solution 2: (Brute Force)**
```
Runtime: 55 ms
Memory: 8.9 MB
```
```c++
class Solution {
public:
    int subarrayGCD(vector<int>& nums, int k) {
        int res = 0;
        for (int i = 0; i < nums.size(); ++i)
            for (int j = i; j < nums.size() && nums[i] % k == 0; ++j) {
                nums[i] = gcd(nums[i], nums[j]);
                res += nums[i] == k;
            }
        return res;
    }
};
```
