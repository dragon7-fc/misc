1658. Minimum Operations to Reduce X to Zero

You are given an integer array `nums` and an integer `x`. In one operation, you can either remove the leftmost or the rightmost element from the array `nums` and subtract its value from `x`. Note that this modifies the array for future operations.

Return the **minimum number** of operations to reduce `x` to **exactly** `0` if it's possible, otherwise, return `-1`.

__Hint1__:

Think in reverse; instead of finding the minimum prefix + suffix, find the maximum subarray.

__Hint2__:

Finding the maximum subarray is standard and can be done greedily.

**Example 1:**
```
Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
```

**Example 2:**
```
Input: nums = [5,6,7,8,9], x = 4
Output: -1
```

**Example 3:**
```
Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
```

**Constraints:**

* `1 <= nums.length <= 105`
* `1 <= nums[i] <= 104`
* `1 <= x <= 109`

# Submissions
---
**Solution 1: (Sliding Window)**
```
Runtime: 1256 ms
Memory Usage: 28.1 MB
```
```python
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target, size, win_sum, lo = sum(nums) - x, -1, 0, -1
        for hi, num in enumerate(nums):
            win_sum += num
            while lo + 1< len(nums) and win_sum > target:
                lo += 1
                win_sum -= nums[lo]
            if win_sum == target:
                size = max(size, hi - lo)
        return -1 if size < 0 else len(nums) - size
```

**Note: DP too slow**

**Solution 2: (Sliding Window)**
```
Runtime: 309 ms
Memory Usage: 98.5 MB
```
```c++
class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        int sum = accumulate(nums.begin(), nums.end(), 0);

		if(sum < x) return -1;
		if(sum == x) return nums.size();

		int target = sum - x, currentSum = 0, start = 0, maxSize = 0;
		for(int i = 0; i < nums.size(); i++) {
			currentSum += nums[i];

			while(currentSum > target)
				currentSum -= nums[start++];

			if(currentSum == target)
				maxSize = max(maxSize, i - start + 1);
		}

		return (maxSize == 0) ? - 1 : nums.size() - maxSize;
    }
};
```
