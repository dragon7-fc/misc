3872. Longest Arithmetic Sequence After Changing At Most One Element

You are given an integer array `nums`.

A **subarray** is **arithmetic** if the difference between consecutive elements in the subarray is constant.

You can replace **at most one** element in `nums` with any integer. Then, you select an arithmetic subarray from `nums`.

Return an integer denoting the maximum length of the arithmetic subarray you can select.

 

**Example 1:**
```
Input: nums = [9,7,5,10,1]

Output: 5

Explanation:

Replace nums[3] = 10 with 3. The array becomes [9, 7, 5, 3, 1].
Select the subarray [9, 7, 5, 3, 1], which is arithmetic because consecutive elements have a common difference of -2.
```

**Example 2:**
```
Input: nums = [1,2,6,7]

Output: 3

Explanation:

Replace nums[0] = 1 with -2. The array becomes [-2, 2, 6, 7].
Select the subarray [-2, 2, 6, 7], which is arithmetic because consecutive elements have a common difference of 4.
```

**Constraints:**

* `4 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^5`

# Submissions
---
**Solution 1: (Prefix Sum, left right, try every position, unit size = 2)**

    nums = [ 9, 7, 5,10, 1]
left         2  2  3  2  2
right        3  2  2  2  2
ans          3  3  3  5  5

```
Runtime: 38 ms, Beats 61.78%
Memory: 227.17 MB, Beats 72.39%
```
```c++
class Solution {
public:
    int longestArithmetic(vector<int>& nums) {
        int n = nums.size(), i;
        if (n <= 2) {
            return n;
        }
        int ans = 2;
        vector<int> left(n, 2);
        vector<int> right(n, 2);
        for (i = 2; i < n; i ++) {
            if (nums[i - 1] - nums[i - 2] == nums[i] - nums[i - 1]) {
                left[i] = left[i - 1] + 1;
            }
        }
        for (i = n - 3; i >= 0; i --) {
            if (nums[i + 2] - nums[i + 1] == nums[i + 1] - nums[i]) {
                right[i] = right[i + 1] + 1;
            }
        }
        // try modify every element
        for (i = 0; i < n; i ++) {
            ans = max(ans, max(left[i], right[i]));
            if (i == 0) {
                ans = max(ans, 1 + right[i + 1]);
            } else if (i == n - 1) {
                ans = max(ans, 1 + left[i - 1]);
            } else  {
                ans = max(ans, 1 + left[i - 1]);
                ans = max(ans, 1 + right[i + 1]);
                if (((nums[i + 1] - nums[i - 1]) % 2) == 0) {
                    int req = (nums[i + 1] - nums[i - 1]) / 2;
                    int leftLen = 1, rightLen = 1;
                    if (i >= 2 && (nums[i - 1] - nums[i - 2] == req)) {
                        leftLen = left[i - 1];
                    }
                    if (i < n - 2 && (nums[i + 2] - nums[i + 1] == req)) {
                        rightLen = right[i + 1];
                    }
                    ans = max(ans, 1 + leftLen + rightLen);
                    //             ^^^^^^^^^^^^^^^^^^^^^^
                    //             1 + left[i - 1] + right[i + 1]
                }
            }
        }
        return ans;
    }
};
```
