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

**Solution 2: (Monotonic Stack, first use mono inc stack to rack min value and range then summation and second use mono dec stack to track max value and range then summation finally subtract max sum with min sum)**

                 x max = stk.top()
             x      x
                       x
                
                --
                   --2--- 
             i-1 i    i+2
sum =     (i-(i-1)) * (i+2-i) * max
            

4           x                 x
1                                     x
-2                x
-3                      x

    nums = [4,   -2,   -3,    4,      1]
stk   #     #,4   #,-2  #,-3  #,-3,4  #,-3,1  #,-3  #
cur               -4    4             -4      -2    27   = 21
                                      
4           x                         x
1                                                          x
-2                x
-3                        x
    nums = [4,   -2,     -3,          4,                   1]
stk   #     #,4  #,4,-2   #,4,-2,-3   #,4,-2  #,4  #  #,4  #,4,1  #,4  #
cur                                   -3      -4   12      1      32  = 38

```
Runtime: 0 ms, Beats 100.00%
Memory: 14.07 MB, Beats 77.06%
```
```c++
class Solution {
public:
    long long subArrayRanges(vector<int>& nums) {
        int n = nums.size(), i, j, i0;
        long long ans = 0;
        stack<int> stk;
        stk.push(-1);
        for (j = 0; j <= n; j ++) {
            while (stk.top() != -1 && (j == n || nums[stk.top()] >= nums[j])) {
                i = stk.top();
                stk.pop();
                i0 = stk.top();
                ans -= (long long)(i - i0) * (j - i) * nums[i];
            }
            stk.push(j);
        }
        stk.pop();
        for (j = 0; j <= n; j ++) {
            while (stk.top() != -1 && (j == n || nums[stk.top()] <= nums[j])) {
                i = stk.top();
                stk.pop();
                i0 = stk.top();
                ans += (long long)(i - i0) * (j - i) * nums[i];
            }
            stk.push(j);
        }
        return ans;
    }
};
```
