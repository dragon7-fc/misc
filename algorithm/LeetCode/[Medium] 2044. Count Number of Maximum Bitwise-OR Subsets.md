2044. Count Number of Maximum Bitwise-OR Subsets

Given an integer array `nums`, find the **maximum** possible **bitwise OR** of a subset of nums and return the **number of different non-empty subsets** with the maximum bitwise OR.

An array `a` is a **subset** of an array `b` if `a` can be obtained from `b` by deleting some (possibly zero) elements of `b`. Two subsets are considered **different** if the indices of the elements chosen are different.

The bitwise OR of an array `a` is equal to `a[0] OR a[1] OR ... OR a[a.length - 1]` (**0-indexed**).

 

**Example 1:**
```
Input: nums = [3,1]
Output: 2
Explanation: The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
- [3]
- [3,1]
```

**Example 2:**
```
Input: nums = [2,2,2]
Output: 7
Explanation: All non-empty subsets of [2,2,2] have a bitwise OR of 2. There are 23 - 1 = 7 total subsets.
```

**Example 3:**
```
Input: nums = [3,2,1,5]
Output: 6
Explanation: The maximum possible bitwise OR of a subset is 7. There are 6 subsets with a bitwise OR of 7:
- [3,5]
- [3,1,5]
- [3,2,5]
- [3,2,1,5]
- [2,5]
- [2,1,5]
```

**Constraints:**

* `1 <= nums.length <= 16`
* `1 <= nums[i] <= 10^5`

# Submissions
---
**Solution 1: (DP Top-Down)**
```
Runtime: 56 ms
Memory Usage: 15.5 MB
```
```python
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        t = functools.reduce(operator.or_, nums)
        N = len(nums)
        
        @functools.lru_cache(None)
        def dp(i, cur):
            if i == N:
                return 0
            rst = 0
            if cur | nums[i] | t == t:
                ncur = cur | nums[i]
                rst += dp(i+1, ncur)
                if ncur == t:
                    rst += 1
            rst += dp(i+1, cur)
            return rst
        
        return dp(0, 0)
```

**Solution 2: (DP Bottom-Up)**
```
Runtime: 120 ms
Memory Usage: 9 MB
```
```c++
class Solution {
public:
    int countMaxOrSubsets(vector<int>& nums) {
        int max = 0, dp[1 << 17] = {1};
        for (int a: nums) {
            for (int i = max; i >= 0; --i)
                dp[i | a] += dp[i];
            max |= a;
        }
        return dp[max];
    }
};
```
