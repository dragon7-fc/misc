3431. Minimum Unlocked Indices to Sort Nums

You are given an array `nums` consisting of integers between 1 and 3, and a binary array `locked` of the same size.

We consider `nums` **sortable** if it can be sorted using adjacent swaps, where a swap between two indices `i` and `i + 1` is allowed if `nums[i] - nums[i + 1] == 1` and `locked[i] == 0`.

In one operation, you can unlock any index `i` by setting `locked[i]` to 0.

Return the **minimum** number of operations needed to make `nums` **sortable**. If it is not possible to make `nums` sortable, return `-1`.

 

**Example 1:**
```
Input: nums = [1,2,1,2,3,2], locked = [1,0,1,1,0,1]

Output: 0

Explanation:

We can sort nums using the following swaps:

swap indices 1 with 2
swap indices 4 with 5
So, there is no need to unlock any index.
```

**Example 2:**
```
Input: nums = [1,2,1,1,3,2,2], locked = [1,0,1,1,0,1,0]

Output: 2

Explanation:

If we unlock indices 2 and 5, we can sort nums using the following swaps:

swap indices 1 with 2
swap indices 2 with 3
swap indices 4 with 5
swap indices 5 with 6
```

**Example 3:**
```
Input: nums = [1,2,1,2,3,2,1], locked = [0,0,0,0,0,0,0]

Output: -1

Explanation:

Even if all indices are unlocked, it can be shown that nums is not sortable.
```
 

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 3`
* `locked.length == nums.length`
* `0 <= locked[i] <= 1`

# Submissions
---
**Solution 1: (Greedy)**

    nums = [1,2,1,2,3,2],
              ^^^   ^^^
              1 2   2 3
cur_max   1   2 
locks     0 0 0 0 0 0 0
ans             0     0    
  locked = [1,0,1,1,0,1]
              ^     ^
--------------------------------
    nums = [1,2,1,1,3,2,2],
              ^^^   ^^^
              1 2   2 3
                ^^^   ^^^
                1 2   2 3
cur_max   1   2 2 2 3 3 3 
locks     0   0 1 0 0 1 0
ans       0     1     2
  locked = [1,0,1,1,0,1,0]
              ^ ^   ^ ^
                1     1
----------------------------------
    nums = [1,2,1,2,3,2,1],
              ^^^   ^^^
              1 2   2 3
                      ^^^
                      1 3
                    xxx
cur_max   1   2 2   3 3 3
locks     0   0 0   0 0
ans                     -1
  locked = [0,0,0,0,0,0,0]
              ^     ^ ^
```
Runtime: 9 ms, Beats 64.29%
Memory: 372.60 MB, Beats 100.00%
```
```c++
class Solution {
public:
    int minUnlockedIndices(vector<int>& nums, vector<int>& locked) {
        int cur_max = 1, locks = 0, res = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (cur_max < nums[i]) {
                cur_max = nums[i];
                locks = 0;
            }
            if (nums[i] < cur_max) {
                if (nums[i] + 1 < cur_max)
                    return -1;                
                res += locks;
                locks = 0;
            }
            locks += locked[i];
        }
        return res;
    }
};
```
