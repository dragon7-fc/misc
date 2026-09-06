4044. Count Good Cyclic Rotations

You are given an integer array `nums` of even length `n`.

A cyclic rotation of `nums` is obtained by choosing a **prefix** of `nums` whose length is between 0 and `n - 1` (inclusive), and moving it to the end of the array while preserving the order of all elements.

A cyclic rotation is **good** if the sum of its first `n / 2` elements is **strictly greater** than the sum of its last `n / 2` elements.

Return the number of cyclic rotations of `nums` that are good.

 

**Example 1:**
```
Input: nums = [1,2,3,4,5,6]

Output: 3

Explanation:

The cyclic rotations of nums are:

Cyclic rotation	Sum of first n / 2 elements	Sum of last n / 2 elements
[1, 2, 3, 4, 5, 6]	1 + 2 + 3 = 6	4 + 5 + 6 = 15
[2, 3, 4, 5, 6, 1]	2 + 3 + 4 = 9	5 + 6 + 1 = 12
[3, 4, 5, 6, 1, 2]	3 + 4 + 5 = 12	6 + 1 + 2 = 9
[4, 5, 6, 1, 2, 3]	4 + 5 + 6 = 15	1 + 2 + 3 = 6
[5, 6, 1, 2, 3, 4]	5 + 6 + 1 = 12	2 + 3 + 4 = 9
[6, 1, 2, 3, 4, 5]	6 + 1 + 2 = 9	3 + 4 + 5 = 12
The first half has a greater sum than the second half for 3 rotations. Thus, the answer is 3.
```

**Example 2:**
```
Input: nums = [1,2,1,2]

Output: 0

Explanation:

The cyclic rotations of nums are:

Cyclic rotation	Sum of first n / 2 elements	Sum of last n / 2 elements
[1, 2, 1, 2]	1 + 2 = 3	1 + 2 = 3
[2, 1, 2, 1]	2 + 1 = 3	2 + 1 = 3
[1, 2, 1, 2]	1 + 2 = 3	1 + 2 = 3
[2, 1, 2, 1]	2 + 1 = 3	2 + 1 = 3
No cyclic rotation is good because the two sums are equal for every rotation. Thus, the answer is 0.
```
 

**Constraints:**

* `2 <= n == nums.length <= 10^5`
* `1 <= nums[i] <= 10^9`
* `n` is even.

# Submissions
---
**Solution 1: (Greedy, Two Pointers)**
```
Runtime: 3 ms, Beats 69.83%
Memory: 103.18 MB, Beats 66.49%
```
```c++
class Solution {
public:
    int countGoodRotations(vector<int>& nums) {
        int n = nums.size();
        int ans = 0;
        long long left = 0;
        long long right = 0;
        for (int i = 0; i < n; i ++) {
            if (i < n / 2) {
                left += nums[i];
            } else {
                right += nums[i];
            }
        }
        ans += left > right;
        int k = n / 2;
        int left_i = 0;
        int right_i = k;
        for (int i = 1; i < n; i ++) {
            left -= nums[left_i];
            left += nums[right_i];
            right -= nums[right_i];
            right += nums[left_i];
            if (left > right) {
                ans += 1;
            }
            left_i = (left_i + 1) % n;
            right_i = (right_i + 1) % n;
        }
        return ans;
    }
};
```

**Solution 2: (Greedy, right = total - left, only check half)**
```
Runtime: 1 ms, Beats 72.37%
Memory: 103.16 MB, Beats 66.49%
```
```c++
class Solution {
public:
    int countGoodRotations(vector<int>& nums) {
        long long total = 0; 
        for (const auto &x: nums) {
            total += x;
        } 
        int n = nums.size();
        long long left = 0;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (i >= n / 2) {
                // Now we have half check if greater than rest half
                long long right = total - left;
                if (left != right) {
                    ans += 1;
                }
                // remove the last one 
                left -= nums[i - n / 2]; 
            }
            left += nums[i]; // rotate 
        }
        return ans; 
    }
};
```
