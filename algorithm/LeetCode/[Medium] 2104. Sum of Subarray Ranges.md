2104. Sum of Subarray Ranges

You are given an integer array `nums`. The **range** of a subarray of `nums` is the difference between the largest and smallest element in the subarray.

Return the **sum of all** subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

 

**Example 1:**
```
Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.
```

**Example 2:**
```
Input: nums = [1,3,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[3], range = 3 - 3 = 0
[3], range = 3 - 3 = 0
[1,3], range = 3 - 1 = 2
[3,3], range = 3 - 3 = 0
[1,3,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.
```

**Example 3:**
```
Input: nums = [4,-2,-3,4,1]
Output: 59
Explanation: The sum of all subarray ranges of nums is 59.
```

**Constraints:**

* `1 <= nums.length <= 1000`
* `-10^9 <= nums[i] <= 10^9`
 

**Follow-up:** Could you find a solution with `O(n)` time complexity?

# Submissions
---
**Solution: (Monotonic Stack)**

    sum(max - min)
= sum(max) - sum(min)

sum(min)
= mono inc stack
      --
    / \--
   /   \-<
  /     \  /
         \/ 

    |--|
    | v|
   x    < 
 x

sum(max)
= mono dec stack

   \  
    \   /-<
     \ /---
   
   x
    x    <
     | ^|  
     |--| 
```
Runtime: 84 ms
Memory: 13.9 MB
```
```python
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n, answer = len(nums), 0 
        stack = []
        
        # Find the sum of all the minimum.
        for right in range(n + 1):
            while stack and (right == n or nums[stack[-1]] >= nums[right]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                answer -= nums[mid] * (mid - left) * (right - mid)
            stack.append(right)

        # Find the sum of all the maximum.
        stack.clear()
        for right in range(n + 1):
            while stack and (right == n or nums[stack[-1]] <= nums[right]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                answer += nums[mid] * (mid - left) * (right - mid)
            stack.append(right)
        
        return answer
```

**Solution 2: (Monotonic Stack)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 14.07 MB, Beats 77.06%
```
```c++
class Solution {
public:
    long long subArrayRanges(vector<int>& nums) {
        int n = nums.size(), i, j, k;
        long long ans = 0;
        stack<int> stk;
        for (j = 0; j <= n; j ++) {
            while (stk.size() && (j == n || nums[stk.top()] >= nums[j])) {
                i = stk.top();
                stk.pop();
                k = stk.size() == 0 ? -1 : stk.top();
                ans -= (long long)(i - k) * (j - i) * nums[i];
            }
            stk.push(j);
        }
        stk.pop();
        for (j = 0; j <= n; j ++) {
            while (stk.size() && (j == n || nums[stk.top()] <= nums[j])) {
                i = stk.top();
                stk.pop();
                k = stk.size() == 0 ? -1 : stk.top();
                ans += (long long)(i - k) * (j - i) * nums[i];
            }
            stk.push(j);
        }
        return ans;
    }
};
```
