3265. Count Almost Equal Pairs I

You are given an array `nums` consisting of positive integers.

We call two integers `x` and `y` in this problem **almost equal** if both integers can become equal after performing the following operation **at most once**:

* Choose **either** `x` or `y` and swap any two digits within the chosen number.

Return the number of indices `i` and `j` in nums where `i < j` such that `nums[i]` and `nums[j]` are **almost equal**.

**Note** that it is allowed for an integer to have leading zeros after performing an operation.

 

**Example 1:**
```
Input: nums = [3,12,30,17,21]

Output: 2

Explanation:

The almost equal pairs of elements are:

3 and 30. By swapping 3 and 0 in 30, you get 3.
12 and 21. By swapping 1 and 2 in 12, you get 21.
```

**Example 2:**
```
Input: nums = [1,1,1,1,1]

Output: 10

Explanation:

Every two elements in the array are almost equal.
```

**Example 3:**
```
Input: nums = [123,231]

Output: 0

Explanation:

We cannot swap any two digits of 123 or 231 to reach the other.
```
 

**Constraints:**

`2 <= nums.length <= 100`
`1 <= nums[i] <= 10^6`

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 106 ms
Memory: 26.68 MB
```
```c++
class Solution {
public:
    int countPairs(vector<int>& nums) {
        int n = nums.size(), mx = *max_element(nums.begin(), nums.end()), m = to_string(mx).size(), ans = 0;
        vector<string> dp(n);
        string cur;
        bool flag;
        for (int i = 0; i < n; i ++) {
            cur = to_string(nums[i]);
            if (cur.size() < m) {
                cur = string(m-cur.size(), '0') + cur;
            }
            dp[i] = cur;
        }
        for (int i = 0; i < n; i ++) {
            for (int j = i+1; j < n; j ++) {
                if (dp[i] == dp[j]) {
                    ans += 1;
                } else {
                    cur = dp[i];
                    flag = false;
                    for (int ii = 0; ii < m; ii ++) {
                        for (int jj = ii+1; jj < m; jj ++) {
                            swap(cur[ii], cur[jj]);
                            if (cur == dp[j]) {
                                flag = true;
                                break;
                            }
                            swap(cur[ii], cur[jj]);
                        }
                        if (flag) {
                            break;
                        }
                    }
                    ans += flag;
                }
            }
        }
        return ans;
    }
};
```
