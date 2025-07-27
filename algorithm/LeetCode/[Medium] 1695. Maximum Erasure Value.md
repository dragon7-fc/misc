1695. Maximum Erasure Value

You are given an array of positive integers nums and want to erase a subarray containing **unique elements**. The score you get by erasing the subarray is equal to the **sum** of its elements.

Return the maximum score you can get by erasing **exactly one** subarray.

An array `b` is called to be a subarray of `a` if it forms a contiguous subsequence of `a`, that is, if it is equal to `a[l],a[l+1],...,a[r]` for some `(l,r)`.

 

**Example 1:**
```
Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].
```

**Example 2:**
```
Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^4`

# Submisskions
---
**Solution 1: (Sliding Window)**
```
Runtime: 1316 ms
Memory Usage: 28.3 MB
```
```python
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = float('-inf')
        cur = 0
        # sliding window; current value = [i, j]
        seen = set()
        i = 0
        for j in range(len(nums)):
            while nums[j] in seen:
                cur -= nums[i]
                seen.remove(nums[i])
                i += 1
            seen.add(nums[j])
            cur += nums[j]
            ans = max(ans, cur)
            
        return ans
```

**Solution 2: (Sliding Window)**
```
Runtime: 4 ms, Beats 98.01%
Memory: 93.62 MB, Beats 97.69%
```
```c++
class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        int n = nums.size(), i = 0, j, a = 0, ans = 0, cnt[10001] = {0};
        for (j = 0; j < n; j ++) {
            cnt[nums[j]] += 1;
            a += nums[j];
            while (cnt[nums[j]] > 1) {
                a -= nums[i];
                cnt[nums[i]] -= 1;
                i += 1;
            }
            ans = max(ans, a);
        }
        return ans;
    }
};
```
