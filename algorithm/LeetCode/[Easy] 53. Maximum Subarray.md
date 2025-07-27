53. Maximum Subarray

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Example 1:**
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
```

**Example 2:**
```
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
```

**Example 3:**
```
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `-10^4 <= nums[i] <= 10^4`
 

**Follow up**: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 60 ms
Memory Usage: N/A
```
```python
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
```

**Solution 2: (DP)**
```
Runtime: 72 ms
Memory Usage: 14.5 MB
```
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        curr_sum = max_sum = nums[0]

        for i in range(1, N):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum
```

**Solution 3: (Divide and Conquer)**
```
Runtime: 164 ms
Memory Usage: 14.6 MB
```
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        def divide(nums, l, r):
            if l == r:
                return nums[l]
            mid = l + (r - l)//2
            lmax = divide(nums, l, mid)
            rmax = divide(nums, mid+1, r)
            rst, cross_left, cross_right = 0, float('-inf'), float('-inf')
            for i in range(mid, l-1, -1):
                rst += nums[i]
                cross_left = max(rst, cross_left)
            rst = 0
            for j in range(mid+1, r+1):
                rst += nums[j]
                cross_right = max(rst, cross_right)
            return max(lmax, rmax, cross_left + cross_right)

        ans = divide(nums, 0, len(nums)-1)
        return ans
```

**Solution 4: (DP)**
```
Runtime: 813 ms
Memory: 28.4 MB
```
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = ans = float('-inf')
        for num in nums:
            pre = max(pre+num, num)
            ans = max(ans, pre)
        return ans
```

**Solution 5: (Greedy)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 71.77 MB, Beats 52.30%
```
```c++
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size(), i, pre = nums[0], ans = pre;
        for (i = 1; i < n; i ++) {
            pre += nums[i];
            if (pre < nums[i]) {
                pre = nums[i];
            }
            ans = max(ans, pre);
        }
        return ans;
    }
};
```
