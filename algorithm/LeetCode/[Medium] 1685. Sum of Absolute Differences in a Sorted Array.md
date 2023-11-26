1685. Sum of Absolute Differences in a Sorted Array

You are given an integer array `nums` sorted in **non-decreasing order**.

Build and return an integer array result with the same length as nums such that `result[i]` is equal to the **summation of absolute differences** between `nums[i]` and all the other elements in the array.

In other words, `result[i]` is equal to `sum(|nums[i]-nums[j]|)` where `0 <= j < nums.length` and `j != i` (**0-indexed**).

 

**Example 1:**
```
Input: nums = [2,3,5]
Output: [4,3,5]
Explanation: Assuming the arrays are 0-indexed, then
result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.
```

**Example 2:**
```
Input: nums = [1,4,6,8,10]
Output: [24,15,13,15,21]
```

**Constraints:**

* `2 <= nums.length <= 105`
* `1 <= nums[i] <= nums[i + 1] <= 104`

# Submissions
---
**Solution 1: (Prefix Sum, Accumulate left and right sight)**
```
Runtime: 892 ms
Memory Usage: 29.7 MB
```
```python
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sumBelow, sumAbove = 0, sum(nums)
        result = []

        for i, num in enumerate(nums):
            sumAbove -= num
            result.append(sumAbove - (n - 1 - i) * num + i * num - sumBelow)
            sumBelow += num

        return result
```

**Solution 2: (prefix sum)**
```
Runtime: 88 ms
Memory: 87.7 MB
```
```c++
class Solution {
public:
    vector<int> getSumAbsoluteDifferences(vector<int>& nums) {
        int n = nums.size(), left = 0, right = 0;
        for (int i = n-1; i >= 0; i --) {
            right += nums[i];
        }
        vector<int> ans;
        for (int i = 0; i < n; i ++) {
            right -= nums[i];
            ans.push_back(right - (n-1-i)*nums[i] + i*nums[i] - left);
            left += nums[i];
        }
        return ans;
    }
};
```
