3728. Stable Subarrays With Equal Boundary and Interior Sum

You are given an integer array `capacity`.

A subarray `capacity[l..r]` is considered **stable** if:

* Its length is at least 3.
* The **first** and **last** elements are each equal to the **sum** of all elements strictly between them (i.e., `capacity[l] = capacity[r] = capacity[l + 1] + capacity[l + 2] + ... + capacity[r - 1]`).

Return an integer denoting the number of **stable** subarrays.

 

**Example 1:**
```
Input: capacity = [9,3,3,3,9]

Output: 2

Explanation:

[9,3,3,3,9] is stable because the first and last elements are both 9, and the sum of the elements strictly between them is 3 + 3 + 3 = 9.
[3,3,3] is stable because the first and last elements are both 3, and the sum of the elements strictly between them is 3.
```

**Example 2:**
```
Input: capacity = [1,2,3,4,5]

Output: 0

Explanation:

No subarray of length at least 3 has equal first and last elements, so the answer is 0.
```

**Example 3:**
```
Input: capacity = [-4,4,0,0,-8,-4]

Output: 1

Explanation:

[-4,4,0,0,-8,-4] is stable because the first and last elements are both -4, and the sum of the elements strictly between them is 4 + 0 + 0 + (-8) = -4
```
 

**Constraints:**

* `3 <= capacity.length <= 10^5`
* `-10^9 <= capacity[i] <= 10^9`

# Submissions
---
**Solution 1: (Prefix Sum, Hash Table)**
```
Runtime: 251 ms, Beats 54.55%
Memory: 216.22 MB, Beats 9.09%
```
```c++
\class Solution {
public:
    long long countStableSubarrays(vector<int>& capacity) {
        int n = capacity.size(), i;
        long long a = 0, b = 0, ans = 0;
        unordered_map<long long, unordered_map<long long, int>> cnt;
        b += capacity[0];
        b += capacity[1];
        for (i = 2; i < n; i ++) {
            a += capacity[i - 2];
            cnt[capacity[i - 2]][a] += 1;
            ans += cnt[capacity[i]][b - capacity[i]];
            b += capacity[i];
        }
        return ans;
    }
};
```
