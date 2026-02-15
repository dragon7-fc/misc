3719. Longest Balanced Subarray I

You are given an integer array `nums`.

A subarray is called balanced if the number of **distinct even** numbers in the subarray is equal to the number of **distinct odd** numbers.

Return the length of the **longest** balanced subarray.

 

**Example 1:**
```
Input: nums = [2,5,4,3]

Output: 4

Explanation:

The longest balanced subarray is [2, 5, 4, 3].
It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [5, 3]. Thus, the answer is 4.
```

**Example 2:**
```
Input: nums = [3,2,2,5,4]

Output: 5

Explanation:

The longest balanced subarray is [3, 2, 2, 5, 4].
It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [3, 5]. Thus, the answer is 5.
```

**Example 3:**
```
Input: nums = [1,2,3,2]

Output: 3

Explanation:

The longest balanced subarray is [2, 3, 2].
It has 1 distinct even number [2] and 1 distinct odd number [3]. Thus, the answer is 3.
```

**Constraints:**

* `1 <= nums.length <= 1500`
* `1 <= nums[i] <= 10^5`

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 1577 ms, Beats 90.36%
Memory: 426.93 MB, Beats 85.54%
```
```c++
class Solution {
public:
    int longestBalanced(vector<int>& nums) {
        int n = nums.size(), i, j, ans = 0;
        unordered_set<int> st_odd, st_even;
        for (i = 0; i < n - 1; i += 1) {
            st_odd.clear();
            st_even.clear();
            for (j = i; j < n; j ++) {
                auto &st = nums[j] % 2 ? st_odd : st_even;
                st.insert(nums[j]);
                if (st_odd.size() == st_even.size()) {
                    ans = max(ans, j - i + 1);
                }
            }
        }
        return ans;
    }
};
```
