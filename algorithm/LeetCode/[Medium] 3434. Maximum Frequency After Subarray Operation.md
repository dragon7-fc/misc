3434. Maximum Frequency After Subarray Operation

You are given an array `nums` of length `n`. You are also given an integer `k`.

You perform the following operation on nums once:

* Select a **subarray**`nums[i..j]` where `0 <= i <= j <= n - 1`.
* Select an integer `x` and add `x` to all the elements in `nums[i..j]`.

Find the **maximum** frequency of the value `k` after the operation.

 

**Example 1:**
```
Input: nums = [1,2,3,4,5,6], k = 1

Output: 2

Explanation:

After adding -5 to nums[2..5], 1 has a frequency of 2 in [1, 2, -2, -1, 0, 1].
```

**Example 2:**
```
Input: nums = [10,2,3,4,5,5,4,3,2,2], k = 10

Output: 4

Explanation:

After adding 8 to nums[1..9], 10 has a frequency of 4 in [10, 10, 11, 12, 13, 13, 12, 11, 10, 10].
```
 

**Constraints:**

* `1 <= n == nums.length <= 10^5`
* `1 <= nums[i] <= 50`
* `1 <= k <= 50`

# Submissions
---
**Solution 1: (Kadane)**

Not sure if it's appropriate to name it as Kadane.

Pick a subarray, count the biggest frequency of any value.
For the rest part of this subarray, count the frequency of k.

This equals to:
Pick a subarray, find out the biggest gap between
the most frequent element and k.

The values range is small,
we can check the every element with kadane alogorithm.

Time O(50n)
Space O(50)


nums = [10,2,3,4,5,5,4,3,2,2], k = 10
--------------------------------------
b       10
cur      0
--------------------------------------
b          2
cur      0 1             2 3
           ^^^^^^^^^^^^^^^^^
--------------------------------------
b            3
cur      0   1         2
             ^^^^^^^^^^^
--------------------------------------
b              4
cur      0     1     2
---------------------------------------
b                5
cur      0       1 2
                 ^^^

count       cur  res
10; 1 <       0
2:  3         3    3 <
3:  2         2
4:  2         2
5:  2         2

```
Runtime: 47 ms, Beats 72.22%
Memory: 96.96 MB, Beats 50.00%
```
```c++
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        for (int a : nums) {
            count[a]++;
        }

        auto kadane = [&](int b) {
            int res = 0, cur = 0;
            for (int a : nums) {
                if (a == k) {
                    cur--;
                }
                if (a == b) {
                    cur++;
                }
                if (cur < 0) {
                    cur = 0;
                }
                res = max(res, cur);
            }
            return res;
        };

        int res = 0;
        for (const auto& [b, _] : count) {
            res = max(res, kadane(b));
        }
        return count[k] + res;
    }
};
```
