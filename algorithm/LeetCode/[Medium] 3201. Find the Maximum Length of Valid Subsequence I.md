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
