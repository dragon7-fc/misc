2012. Sum of Beauty in the Array

You are given a **0-indexed** integer array `nums`. For each index `i` (`1 <= i <= nums.length - 2`) the **beauty** of `nums[i]` equals:

* `2`, if `nums[j] < nums[i] < nums[k]`, for **all** `0 <= j < i` and for **all** `i < k <= nums.length - 1`.
* `1`, if `nums[i - 1] < nums[i] < nums[i + 1]`, and the previous condition is not satisfied.
* `0`, if none of the previous conditions holds.

Return the **sum of beauty** of all `nums[i]` where `1 <= i <= nums.length - 2`.

 

**Example 1:**
```
Input: nums = [1,2,3]
Output: 2
Explanation: For each index i in the range 1 <= i <= 1:
- The beauty of nums[1] equals 2.
```

**Example 2:**
```
Input: nums = [2,4,6,4]
Output: 1
Explanation: For each index i in the range 1 <= i <= 2:
- The beauty of nums[1] equals 1.
- The beauty of nums[2] equals 0.
```

**Example 3:**
```
Input: nums = [3,2,1]
Output: 0
Explanation: For each index i in the range 1 <= i <= 1:
- The beauty of nums[1] equals 0.
```

**Constraints:**

* `3 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^5`

# Submissions
---
**Solution 1: (Prefix Sum)**
```
Runtime: 1172 ms
Memory Usage: 28.2 MB
```
```python
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n, sm = len(nums), 0
        mi, mx = [0] * n + [math.inf], [0] * (n + 1)
        for i, num in enumerate(nums):
            mx[i + 1] = max(num, mx[i])
            mi[~i - 1] = min(nums[~i], mi[~i])
        for i in range(1, len(nums) - 1):
            if mx[i] < nums[i] < mi[i + 1]:
                sm += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                sm += 1
        return sm 
```

**Solution 2: (Prefix Sum)**
```
Runtime: 148 ms
Memory Usage: 88.5 MB
```
```c++
class Solution {
public:
    int sumOfBeauties(vector<int>& nums) {
        int n=nums.size();
        
        vector<int> left(n);
        vector<int> right(n);
        
        left[0]=nums[0];
        right[n-1]=nums[n-1];
        
        for(int i=1; i<n; i++)
        {
            left[i]=max(left[i-1],nums[i]);
        }
        for(int i=n-2; i>=0; i--)
        {
            right[i]=min(nums[i],right[i+1]);
        }
        
        int count=0;
        
        for(int i=1; i<n-1; i++)
        {            
            if(left[i-1] < nums[i] && nums[i] < right[i+1])
            {
                count+=2;
            }
            else if(nums[i-1] < nums[i] && nums[i] < nums[i+1])
            {
                count++;
            }
        }
        
        return count;
    }
};
```
