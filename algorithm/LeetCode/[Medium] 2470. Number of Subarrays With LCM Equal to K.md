2470. Number of Subarrays With LCM Equal to K

Given an integer array `nums` and an integer `k`, return the number of **subarrays** of `nums` where the least common multiple of the subarray's elements is `k`.

A **subarray** is a contiguous non-empty sequence of elements within an array.

The **least common multiple of an array** is the smallest positive integer that is divisible by all the array elements.

 

**Example 1:**
```
Input: nums = [3,6,2,7,1], k = 6
Output: 4
Explanation: The subarrays of nums where 6 is the least common multiple of all the subarray's elements are:
- [3,6,2,7,1]
- [3,6,2,7,1]
- [3,6,2,7,1]
- [3,6,2,7,1]
```

**Example 2:**
```
Input: nums = [3], k = 2
Output: 0
Explanation: There are no subarrays of nums where 2 is the least common multiple of all the subarray's elements.
```

**Constraints:**

* `1 <= nums.length <= 1000`
* `1 <= nums[i], k <= 1000`

# Submissions
---
**Solution 1: (prefix sum)**
```
Runtime: 1355 ms
Memory: 14 MB
```
```python
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        cnt = 0

        for i in range(0, len(nums)):       # [1] for every initial number, try extending
            l = nums[i]                     #     a continuous sequence of numbers
            for j in range(i, len(nums)):  
                l = lcm(l,nums[j])          # [2] once LCM becomes 'k', each subsequent number
                if l == k : cnt += 1        #     that don't increase this value will give one
                if l > k  : break           #     more valid subarray
            
        return cnt
```

**Solution 1: (prefix sum)**
```
Runtime: 64 ms
Memory: 9.3 MB
```
```c++
class Solution {
public:
    int subarrayLCM(vector<int>& nums, int k) {
        int ans = 0;
        for(int i = 0; i < nums.size(); ++i){
            int mx = nums[i], t;
            for(int j = i; j < nums.size(); ++j){
                t = lcm(mx, nums[j]);
                if(t == k){
                    ans++;
                    mx = max(mx, nums[j]);
                }
                else if( t == 1) continue;
                else if( i != j ) break;
            }
        }
        return ans;
    }
};
```
