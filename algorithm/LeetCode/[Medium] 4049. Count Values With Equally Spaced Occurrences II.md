4049. Count Values With Equally Spaced Occurrences II

You are given an integer array `nums`.

An integer `x` is called **special** if:

* `x` appears at least three times in `nums`.
* All occurrences of `x` are equally spaced in `nums`. In other words, if all occurrences of `x` are at indices `i_1 < i_2 < ... < i_m`, then `i_2 - i_1 = i_3 - i_2 = ... = i_m - i_m-1`.

Return the number of distinct special integers in `nums`.

 

**Example 1:**
```
Input: nums = [1,8,1,5,1,5,8,5]

Output: 2

Explanation:

1 is special because it occurs at equally spaced indices 0, 2, and 4.
5 is special because it occurs at equally spaced indices 3, 5, and 7.
8 is not special because it occurs only twice.
Therefore, the answer is 2.
```

**Example 2:**
```
Input: nums = [8,8,8,8]

Output: 1

Explanation:

8 is special because it occurs at equally spaced indices 0, 1, 2, and 3. Therefore, the answer is 1.
```

**Example 3:**
```
Input: nums = [8,6,6,8,8]

Output: 0

Explanation:

8 occurs at indices 0, 3, and 4, which are not equally spaced. 6 occurs only twice. Therefore, no integer is special.
```
 

**Constraints:**

* `3 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (Prefix Sum)**
```
Runtime: 224 ms, Beats 50.00%
Memory: 294.02 MB, Beats 100.00%
```
```c++
class Solution {
public:
    int countSpecialIntegers(vector<int>& nums) {
        unordered_map<int, vector<int>> mp;
        for (int i = 0; i < nums.size(); i ++) {
            mp[nums[i]].push_back(i);
        }
        int ans = 0;
        for (const auto& [_, dp]: mp) {
            if (dp.size() >= 3) {
                bool flag = true;
                for (int i = 1; i < dp.size() - 1; i ++) {
                    if (dp[i] - dp[i - 1] != dp[i + 1] - dp[i]) {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    ans += 1;
                }
            }
        }
        return ans;
    }
};
```
