3201. Find the Maximum Length of Valid Subsequence I

You are given an integer array `nums`. A subsequence `sub` of `nums` with length `x` is called **valid** if it satisfies:

* `(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2`.

Return the length of the **longest valid** subsequence of `nums`.

A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

**Example 1:**
```
Input: nums = [1,2,3,4]

Output: 4

Explanation:

The longest valid subsequence is [1, 2, 3, 4].
```

**Example 2:**
```
Input: nums = [1,2,1,1,2,1,2]

Output: 6

Explanation:

The longest valid subsequence is [1, 2, 1, 2, 1, 2].
```

**Example 3:**
```
Input: nums = [1,3]

Output: 2

Explanation:

The longest valid subsequence is [1, 3].
```
 

**Constraints:**

* `2 <= nums.length <= 2 * 10^5`
* `1 <= nums[i] <= 10^7`

# Submissions
---
**Solution 1: (DP Bottom-Up, Odd Even Toggle Parity)**

(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2
-> sub[0]%2 == sub[2]%2

```
Runtime: 97 ms
Memory: 94.21 MB
```
```c++
class Solution {
public:
    int maximumLength(vector<int>& nums) {
        int c = nums[0] % 2, odd = 0, even = 0, both = 0;
        for (int num : nums) {
            if (num % 2 == 0) {
                even++;
            } else {
                odd++;
            }
            if (num % 2 == c) {
                both++;
                c = 1 - c;  // Toggle the parity
            }
        }
        return max(both, max(even, odd));
    }
};
```

**Solution 2: (Brute Force, Parity of Enumeration Elements)**
```
Runtime: 21 ms, Beats 19.12%
Memory: 97.16 MB, Beats 25.00%
```
```c++
class Solution {
public:
    int maximumLength(vector<int>& nums) {
        int res = 0;
        vector<vector<int>> patterns = {{0, 0}, {0, 1}, {1, 0}, {1, 1}};
        for (auto& pattern : patterns) {
            int cnt = 0;
            for (int num : nums) {
                if (num % 2 == pattern[cnt % 2]) {
                    cnt++;
                }
            }
            res = max(res, cnt);
        }
        return res;
    }
};
```

**Solution 3: (DP Bottom-Up)**

      1,2,3,4
00      1   2
01      1 3
10      2   4
11      1 2

              v 
    1,2,1,1,2,1,2
    ^ ^ ^   ^ ^ ^
00    1     2   3
01    1 3 3   5
10    2     4   6
11    1 2 3   4

    1 3
e     
o   1 2
    
    1 1 3 9 5
00
01    1 1 1 1
10   
11    2 3 4 5

```
Runtime: 2 ms, Beats 77.94%
Memory: 96.26 MB, Beats 40.00%
```
```c++
class Solution {
public:
    int maximumLength(vector<int>& nums) {
        int n = nums.size(), i;
        vector<int> dp(4);
        if (nums[0]%2 == 0 || nums[1]%2 == 0) {
            dp[0] |= 1;
            dp[2] |= 1;
        }
        if (nums[0]%2 || nums[1]%2) {
            dp[1] |= 1;
            dp[3] |= 1;
        }
        dp[((nums[0]%2)<<1) + nums[1]%2] += 1;
        for (i = 2; i < n; i ++) {
            if (nums[i]%2) {
                dp[3] += 1;
                dp[1] = max(dp[1], dp[2] + 1);
            } else {
                dp[0] += 1;
                dp[2] = max(dp[2], dp[1] + 1);
            }
        }
        return *max_element(dp.begin(), dp.end());
    }
};
```
