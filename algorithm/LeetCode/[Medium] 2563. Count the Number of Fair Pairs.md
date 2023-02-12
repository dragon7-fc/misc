2563. Count the Number of Fair Pairs

Given a **0-indexed** integer array `nums` of size `n` and two integers `lower` and `upper`, return the number of fair pairs.

A pair `(i, j)` is **fair** if:

* `0 <= i < j < n`, and
* `lower <= nums[i] + nums[j] <= upper`
 

**Example 1:**
```
Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
```

**Example 2:**
```
Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `nums.length == n`
* `-10^9 <= nums[i] <= 10^9`
* `-10^9 <= lower <= upper <= 10^9`

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 948 ms
Memory: 29 MB
```
```python
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        right = len(nums) - 1
        count = 0
        while right > 0:
            start = bisect.bisect_left(nums, lower - nums[right], 0, right)
            end = bisect.bisect_right(nums, upper - nums[right], 0, right) - 1
            if end >= start:
                count += end - start + 1
            right -= 1
        return count
```

**Solution 1: (Binary Search)**
```
Runtime: 292 ms
Memory: 53.5 MB
```
```c++
class Solution {
public:
    long long countFairPairs(vector<int>& nums, int lower, int upper) {
        sort(nums.begin(),nums.end());
        long long ans = 0;
        for(int i = nums.size() - 1; i >= 0; i--) {
            int vl = lower - nums[i], vu = upper - nums[i];
            auto left = lower_bound(nums.begin(),nums.begin()+i, vl);
            auto right = upper_bound(nums.begin(), nums.begin()+i, vu);
            ans += (right-left);
        }
        return ans;
    }
};
```
