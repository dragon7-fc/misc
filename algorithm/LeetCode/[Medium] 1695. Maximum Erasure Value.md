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
Runtime: 488 ms
Memory Usage: 127 MB
```
```c++
class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        unordered_set<int> st;
        int i = 0, cur = 0, ans = 0;
        for (int j = 0; j < nums.size(); j ++) {
            while (st.count(nums[j])) {
                cur -= nums[i];
                st.erase(nums[i]);
                i += 1;
            }
            cur += nums[j];
            st.insert(nums[j]);
            ans = max(ans, cur);
        }
        return ans;
    }
};
```
