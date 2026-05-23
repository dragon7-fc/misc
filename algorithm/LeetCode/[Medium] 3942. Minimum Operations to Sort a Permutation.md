3942. Minimum Operations to Sort a Permutation

You are given an integer array `nums` of length `n`, where `nums` is a **permutation** of the integers from 0 to `n - 1`.

You may perform only the following operations:

* **Reverse** the entire array.
* **Rotate Left by One**: Move the first element to the end of the array, and rest elements to left by one position.

Return an integer denoting the **minimum** number of operations required to sort the array in **increasing** order. If it is **not possible** to sort the array using only the given operations, return -1.

 

**Example 1:**
```
Input: nums = [0,2,1]

Output: 2

Explanation:

Rotate Left by one: [2, 1, 0]
Reverse the array: [0, 1, 2]
The array becomes sorted in 2 operations, which is minimal
```

**Example 2:**
```
Input: nums = [1,0,2]

Output: 2

Explanation:

Reverse the array: [2, 0, 1]
Rotate Left by one: [0, 1, 2]
The array becomes sorted in 2 operations, which is minimal.
```

**Example 3:**
```
Input: nums = [2,0,1,3]

Output: -1

Explanation:

It is impossible to reach [2, 0, 1, 3]. Thus, the answer is -1.
```
 

**Constraints:**

* `1 <= n == nums.length <= 10^5`
* `0 <= nums[i] <= n - 1`
*r `nums` is a permutation of integers from 0 to `n - 1`.

# Submissions
---
**Solution 1: (Case Study)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 141.36 MB, Beats 90.18%
```
```c++
class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size(), left, i, j, k;
        if (n == 1) {
            return 0;
        }
        left = find(nums.begin(), nums.end(), 0) - nums.begin();
        // increasing
        if (nums[(left + 1) % n] == nums[left] + 1) {
            i = left;
            for (int k = 1; k < n - 1; k ++) {
                j = (i + k) % n;
                if (nums[j] != nums[i] + k) {
                    return -1;
                }
            }
            return min({left, 1 + (n - (left - 1 + n) % n) - 1 + 1});
                       // rotate left
                              // reverse + rotate left + reverse

        // decreasing
        } else if (nums[(left - 1 + n) % n] == nums[left] + 1) {
            i = left;
            for (int k = 1; k < n - 1; k ++) {
                j = (i - k + n) % n;
                if (nums[j] != nums[i] + k) {
                    return -1;
                }
            }
            return min((left + 1) % n + 1, 1 + n - ((left + 1) % n));
                        // rotate left + reverse
                                           // reverse + rotate left
        } else {
            return -1;
        }
    }
};
```
