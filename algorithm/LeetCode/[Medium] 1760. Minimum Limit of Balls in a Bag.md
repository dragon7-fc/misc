1760. Minimum Limit of Balls in a Bag

You are given an integer array `nums` where the `i`th bag contains `nums[i]` balls. You are also given an integer `maxOperations`.

You can perform the following operation at most `maxOperations` times:

* Take any bag of balls and divide it into two new bags with a positive number of balls.
    * For example, a bag of `5` balls can become two new bags of `1` and `4` balls, or two new bags of `2` and `3` balls.

Your penalty is the maximum number of balls in a bag. You want to minimize your penalty after the operations.

Return the minimum possible penalty after performing the operations.

 

**Example 1:**
```
Input: nums = [9], maxOperations = 2
Output: 3
Explanation: 
- Divide the bag with 9 balls into two bags of sizes 6 and 3. [9] -> [6,3].
- Divide the bag with 6 balls into two bags of sizes 3 and 3. [6,3] -> [3,3,3].
The bag with the most number of balls has 3 balls, so your penalty is 3 and you should return 3.
```

**Example 2:**
```
Input: nums = [2,4,8,2], maxOperations = 4
Output: 2
Explanation:
- Divide the bag with 8 balls into two bags of sizes 4 and 4. [2,4,8,2] -> [2,4,4,4,2].
- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,4,4,4,2] -> [2,2,2,4,4,2].
- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,4,4,2] -> [2,2,2,2,2,4,2].
- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,2,2,4,2] -> [2,2,2,2,2,2,2,2].
The bag with the most number of balls has 2 balls, so your penalty is 2 an you should return 2.
```

**Example 3:**
```
Input: nums = [7,17], maxOperations = 2
Output: 7
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= maxOperations, nums[i] <= 10^9`

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 1224 ms
Memory Usage: 26.9 MB
```
```python
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if sum((a - 1) // mid for a in nums) > maxOperations:
                left = mid + 1
            else:
                right = mid
        return left
```

**Solution 2: (Binary Search)**
```
Runtime: 27 ms
Memory: 59.79 MB
```
```c++
class Solution {
    bool check(int mid, vector<int> &nums, int maxOperations) {
        int cur = 0;
        for (auto &num: nums) {
            cur += (num-1) / mid;
            if (cur > maxOperations) {
                return false;
            }
        }
        return true;
    }
public:
    int minimumSize(vector<int>& nums, int maxOperations) {
        int lo = 1, hi = *max_element(nums.begin(), nums.end()), mid, ans = INT_MAX;
        while (lo <= hi) {
            mid = lo + (hi-lo)/2;
            if (!check(mid, nums, maxOperations)) {
                lo = mid+1;
            } else {
                ans = min(ans, mid);
                hi = mid-1;
            }
        }
        return ans;
    }
};
```
