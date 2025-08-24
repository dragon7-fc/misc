1493. Longest Subarray of 1's After Deleting One Element

Given a binary array `nums`, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array.

Return 0 if there is no such subarray.

 

**Example 1:**
```
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
```

**Example 2:**
```
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
```

**Example 3:**
```
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
```

**Example 4:**
```
Input: nums = [1,1,0,0,1,1,1,0,1]
Output: 4
```

**Example 5:**
```
Input: nums = [0,0,0]
Output: 0
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `nums[i]` is either `0` or `1`.

# Submissions
---
**Solution 1: (Sliding Window)**

1. Use `i` and `j` as the lower and upper bounds, both inclusively;
1. Loop through the nums by upper bound, accumulate current element on the sum, then check if sum is less than `j - i` (which implies the window includes at least 2 0s) : if yes, keep increase the lower bound `i` till either the sliding window has at most 1 zero or lower bound is same as upper bound;
1. Update the max value of the sliding window.

```
Runtime: 472 ms
Memory Usage: 16.2 MB
```
```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = sum = lo = 0
        for hi, num in enumerate(nums):
            sum += num
            while lo < hi and sum < hi - lo:
                sum -= nums[lo]
                lo += 1
            ans = max(ans, hi - lo)
        return ans  
```

**Solution 2: (Sliding Window)**
```
Runtime: 108 ms
Memory Usage: 36.5 MB
```
```c++
class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int i = 0, j, k = 1;
        for (j = 0; j < nums.size(); ++j) {
            if (nums[j] == 0) k--;
            if (k < 0 && nums[i++] == 0) k++;
        }
        return j - i - 1;
    }
};
```

**Solution 3: (Sliding Window)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 60.10 MB, Beats 23.29%
```
```c++
class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int n = nums.size(), i = 0, j, one = 0, zero = 0, ans = 0;
        for (j = 0; j < n; j ++) {
            if (nums[j]) {
                one += 1;
            } else {
                zero += 1;
            }
            while (zero > 1) {
                if (nums[i]) {
                    one -= 1;
                } else {
                    zero -= 1;
                }
                i += 1;
            }
            ans = max(ans, one);
        }
        return min(n-1, ans);
    }
};
```
