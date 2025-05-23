2501. Longest Square Streak in an Array

You are given an integer array `nums`. A subsequence of nums is called a square streak if:

* The length of the subsequence is at least `2`, and
* **after** sorting the subsequence, each element (except the first element) is the **square** of the previous number.

Return the length of the **longest square streak** in `nums`, or return `-1` if there is no **square streak**.

A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

**Example 1:**
```
Input: nums = [4,3,6,16,8,2]
Output: 3
Explanation: Choose the subsequence [4,16,2]. After sorting it, it becomes [2,4,16].
- 4 = 2 * 2.
- 16 = 4 * 4.
Therefore, [4,16,2] is a square streak.
It can be shown that every subsequence of length 4 is not a square streak.
```

**Example 2:**
```
Input: nums = [2,3,5,6,7]
Output: -1
Explanation: There is no square streak in nums so return -1.
```

**Constraints:**

* `2 <= nums.length <= 10^5`
* `2 <= nums[i] <= 10^5`

# Submissions
---
**Solution 1: (Sort, Hash Table)**
```
Runtime: 1374 ms
Memory: 33 MB
```
```python
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        sorted_nums = sorted(list(set(nums)))
        N = len(sorted_nums)
        dp = {}
        dp[sorted_nums[0]] = 1
        ans = -1
        for i in range(1, N):
            if sorted_nums[i]**.5 in dp:
                dp[sorted_nums[i]] = dp[sorted_nums[i]**.5] + 1
                ans = max(ans, dp[sorted_nums[i]])
            else:
                dp[sorted_nums[i]] = 1
        return ans
```

**Solution 2: (Set)**
```
Runtime: 82 ms
Memory: 108.97 MB
```
```c++
class Solution {
public:
    int longestSquareStreak(vector<int>& nums) {
        unordered_set<int> st(nums.begin(), nums.end());
        long long cur;
        int k, ans = 0;
        for (auto num: st) {
            cur = num;
            k = 0;
            while (cur <= 1e5 && st.count(cur)) {
                k += 1;
                cur *= cur;
            }
            ans = max(ans, k);
        }
        return ans != 1 ? ans : -1;
    }
};
```
