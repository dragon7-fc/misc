3514. Number of Unique XOR Triplets II

You are given an integer array `nums`.

A **XOR triplet** is defined as the XOR of three elements `nums[i] XOR nums[j] XOR nums[k]` where `i <= j <= k`.

Return the number of **unique** XOR triplet values from all possible triplets `(i, j, k)`.

 

**Example 1:**
```
Input: nums = [1,3]

Output: 2

Explanation:

The possible XOR triplet values are:

(0, 0, 0) → 1 XOR 1 XOR 1 = 1
(0, 0, 1) → 1 XOR 1 XOR 3 = 3
(0, 1, 1) → 1 XOR 3 XOR 3 = 1
(1, 1, 1) → 3 XOR 3 XOR 3 = 3
The unique XOR values are {1, 3}. Thus, the output is 2.
```

**Example 2:**
```
Input: nums = [6,7,8,9]

Output: 4

Explanation:

The possible XOR triplet values are {6, 7, 8, 9}. Thus, the output is 4.
```
 

**Constraints:**

* `1 <= nums.length <= 1500`
* `1 <= nums[i] <= 1500`

# Submissions
---
**Solution 1: (Set)**

    0 1 1 0<
    0 1 1 1<
    1 0 0 0
    1 0 0 1

    1 14 15
    7 9

```
Runtime: 2651 ms, Beats 8.57%
Memory: 100.38 MB, Beats 71.43%
```
```c++
class Solution {
public:
    int uniqueXorTriplets(vector<int>& nums) {
        int n = nums.size(), i, j;
        unordered_set<int> st, st2;
        for (i = 0; i < n; i ++) {
            for (j = 0; j < n; j ++) {
                st.insert(nums[i]^nums[j]);
            }
        }
        for (auto a: nums) {
            for (auto b: st) {
                st2.insert(a^b);
            }
        }
        return st2.size();
    }
};
```
