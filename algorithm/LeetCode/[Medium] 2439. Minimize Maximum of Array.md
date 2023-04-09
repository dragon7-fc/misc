2439. Minimize Maximum of Array

You are given a **0-indexed** array `nums` comprising of `n` non-negative integers.

In one operation, you must:

* Choose an integer `i` such that `1 <= i < n` and `nums[i] > 0`.
* Decrease `nums[i]` by `1`.
* Increase `nums[i - 1]` by `1`.

Return the **minimum** possible value of the **maximum** integer of `nums` after performing any number of operations.

 

**Example 1:**
```
Input: nums = [3,7,1,6]
Output: 5
Explanation:
One set of optimal operations is as follows:
1. Choose i = 1, and nums becomes [4,6,1,6].
2. Choose i = 3, and nums becomes [4,6,2,5].
3. Choose i = 1, and nums becomes [5,5,2,5].
The maximum integer of nums is 5. It can be shown that the maximum number cannot be less than 5.
Therefore, we return 5.
```

**Example 2:**
```
Input: nums = [10,1]
Output: 10
Explanation:
It is optimal to leave nums as is, and since 10 is the maximum value, we return 10.
```

**Constraints:**

* `n == nums.length`
* `2 <= n <= 10^5`
* `0 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (Prefix Sum Average)**
```
Runtime: 2318 ms
Memory: 26.1 MB
```
```python
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        return max(ceil(n / (i + 1)) for i, n in enumerate(accumulate(nums)))
```

**Solution 2: (Prefix Sum Average)**
```
Runtime: 134 ms
Memory: 71.4 MB
```
```c++
class Solution {
public:
    int minimizeArrayValue(vector<int>& nums) {
        long sum = 0, res = 0;
        for (int i = 0; i < nums.size(); ++i) {
            sum += nums[i];
            res = max(res, (long) ceil(sum*1.0 / (i + 1)));
        }
        return res;
    }
};
```

**Solution 3: (Binary Search)**
```
Runtime: 139 ms
Memory: 71.3 MB
```
```c++
class Solution {
    bool check(vector<int> &nums, int k) {
        long long have = 0;
        for (int num: nums) {
            if (num <= k) {
                have += k-num;
            } else {
                if (have < num-k)
                    return false; 
                else
                    have -= (num-k);
            }
        }
        return true;
    }
public:
    int minimizeArrayValue(vector<int>& nums) {
        int left = 0, right = *max_element(nums.begin(), nums.end()), mid;
        while (left<right) { 
            mid = left + (right-left)/2;
            if (check(nums, mid))
                right = mid;
            else
                left = mid + 1;
        }
        return left;
    }
};
```
