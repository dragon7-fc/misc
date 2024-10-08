1590. Make Sum Divisible by P

Given an array of positive integers `nums`, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by `p`. It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or `-1` if it's impossible.

A subarray is defined as a contiguous block of elements in the array.

 

**Example 1:**
```
Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.
```

**Example 2:**
```
Input: nums = [6,3,5,2], p = 9
Output: 2
Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.
```

**Example 3:**
```
Input: nums = [1,2,3], p = 3
Output: 0
Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.
```

**Example 4:**
```
Input: nums = [1,2,3], p = 7
Output: -1
Explanation: There is no way to remove a subarray in order to get a sum divisible by 7.
```

**Example 5:**
```
Input: nums = [1000000000,1000000000,1000000000], p = 3
Output: 0
```

**Constraints:**

* `1 <= nums.length <= 105`
* `1 <= nums[i] <= 109`
* `1 <= p <= 109`

# Submissions
---
**Solution 1: (Prefix Sum, Hash Table, Prefix sum Hash Table index)**
```
Runtime: 772 ms
Memory Usage: 32.3 MB
```
```python
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        need = sum(nums) % p
        dp = {0: -1}
        cur = 0
        res = n = len(nums)
        for i, a in enumerate(nums):
            cur = (cur + a) % p
            dp[cur] = i
            if (cur - need) % p in dp:
                res = min(res, i - dp[(cur - need) % p])
        return res if res < n else -1
```

**Solution 1: (Prefix Sum, Hash Table, Prefix sum Hash Table index)**
```
Runtime: 124 ms
Memory: 70.48 MB
```
```c++
class Solution {
public:
    int minSubarray(vector<int>& nums, int p) {
        unordered_map<int, int> dp;
        dp[0] = -1;
        long long cur = 0;
        int d = accumulate(nums.begin(), nums.end(), 0L)%p, n = nums.size(), ans = n;
        if (d == 0) {
            return 0;
        }
        for (int i = 0; i < n; i ++) {
            cur +=  nums[i];
            if (dp.count(((cur-d)%p + p)%p)) {
                ans = min(ans, i - dp[((cur-d)%p + p)%p]);
            }
            dp[cur%p] = i;
        }
        return ans == n ? -1 : ans;
    }
};
```
