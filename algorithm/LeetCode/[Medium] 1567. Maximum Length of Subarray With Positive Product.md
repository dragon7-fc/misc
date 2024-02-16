1567. Maximum Length of Subarray With Positive Product

Given an array of integers `nums`, find the maximum length of a subarray where the product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

Return the maximum length of a subarray with positive product.

 

**Example 1:**
```
Input: nums = [1,-2,-3,4]
Output: 4
Explanation: The array nums already has a positive product of 24.
```

**Example 2:**
```
Input: nums = [0,1,-2,-3,-4]
Output: 3
Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.
```

**Example 3:**
```
Input: nums = [-1,-2,-3,0,1]
Output: 2
Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].
```

**Example 4:**
```
Input: nums = [-1,2]
Output: 1
```

**Example 5:**
```
Input: nums = [1,2,3,5,-6,4,0,10]
Output: 4
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `-10^9 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 660 ms
Memory Usage: 27.9 MB
```
```python
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = pos = neg = 0
        for x in nums: 
            if x > 0: pos, neg = 1 + pos, 1 + neg if neg else 0
            elif x < 0: pos, neg = 1 + neg if neg else 0, 1 + pos
            else: pos = neg = 0 # reset 
            ans = max(ans, pos)
        return ans
```

**Solution 2: (Greedy)**
```
Runtime: 84 ms
Memory: 60.16 MB
```
```c++
class Solution {
public:
    int getMaxLen(vector<int>& nums) {
        int posLen = 0, negLen = 0, maxLen = 0;
        for (int i : nums) {
            if (i == 0) posLen = 0, negLen = 0;
            else {
                if (i < 0) swap(posLen, negLen);
                if (posLen > 0 || i > 0) ++posLen;
                if (negLen > 0 || i < 0) ++negLen;
                maxLen = max(maxLen, posLen);
            }
        }
        return maxLen;
    }
};
```
