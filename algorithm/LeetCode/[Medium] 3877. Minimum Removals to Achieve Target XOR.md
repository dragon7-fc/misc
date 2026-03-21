3877. Minimum Removals to Achieve Target XOR

You are given an integer array `nums` and an integer `target`.

You may remove any number of elements from `nums` (possibly zero).

Return the **minimum** number of removals required so that the bitwise `XOR` of the remaining elements equals `target`. If it is impossible to achieve `target`, return `-1`.

The bitwise `XOR` of an empty array is `0`.

 

**Example 1:**
```
Input: nums = [1,2,3], target = 2

Output: 1

Explanation:

Removing nums[1] = 2 leaves [nums[0], nums[2]] = [1, 3].
The XOR of [1, 3] is 2, which equals target.
It is not possible to achieve XOR = 2 in less than one removal, therefore the answer is 1.
```

**Example 2:**
```
Input: nums = [2,4], target = 1

Output: -1

Explanation:

It is impossible to remove elements to achieve target. Thus, the answer is -1.
```

**Example 3:**
```
Input: nums = [7], target = 7

Output: 0

Explanation:

The XOR of all elements is nums[0] = 7, which equals target. Thus, no removal is needed.
```
 

**Constraints:**

* `1 <= nums.length <= 40`
* `0 <= nums[i] <= 10^4`
* `0 <= target <= 10^4`

# Submissions
---
**Solution 1: (Hash Table, DP Bottom Up, SubSets)**

__Intuition__
We want to find a subset with XOR sum equal to XOR(A) ^ target.
where XOR is the total XOR sum of all elements.

__Explanation__
The DP tracks the minimum size for each subset XOR sum.
We iterate through each element and update the DP map.
The target is updated during this process.
Finally, we return the dp[target].

__Complexity__
Time O(40 x 1000)
Space O(40 x 1000)

    nums = [1,2,3], target = 2
target: 2
dp
0   0
-------------------------------
            i
a: 1
target: 3
dp:
0   0
1   1
--------------------------------
              i
a: 2
target: 1
dp:
0   0
1   1
2   1
3   2
--------------------------------
                i
a: 3
target: 2
dp:
0   0
1   1
2   1   < ans
3   1

        v        nums
dp      1  2  3
0    0
1       1
2          1
3          2  1



dp      a  b  c
0   0
a       1
b          1
ab         2
c             1
ac            1
bc            1
abc           2



```
Runtime: 120 ms, Beats 90.80%
Memory: 78.83 MB, Beats 70.38%
```
```c++
class Solution {
public:
    int minRemovals(vector<int>& nums, int target) {
        unordered_map<int, int> pre;
        pre[0] = 0;
        for (int a : nums) {
            target ^= a;
            vector<pair<int, int>> dp(pre.begin(), pre.end());
            for (auto &[v, c] : dp) {
                int nv = v ^ a;
                int nc = pre.count(nv) ? pre[nv] : 50;
                if (c + 1 < nc) {
                    pre[nv] = c + 1;
                }
            }
        }
        return pre.count(target) ? pre[target] : -1;
    }
};
```
