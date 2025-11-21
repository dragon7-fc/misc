3752. Lexicographically Smallest Negated Permutation that Sums to Target

You are given a positive integer `n` and an integer `target`.

Return the **lexicographically smallest** array of integers of size `n` such that:

* The sum of its elements equals `target`.
* The absolute values of its elements form a **permutation** of size `n`.

If no such array exists, return an empty array.

A **permutation** of size `n` is a rearrangement of integers `1, 2, ..., n`.

 

**Example 1:**
```
Input: n = 3, target = 0

Output: [-3,1,2]

Explanation:

The arrays that sum to 0 and whose absolute values form a permutation of size 3 are:

[-3, 1, 2]
[-3, 2, 1]
[-2, -1, 3]
[-2, 3, -1]
[-1, -2, 3]
[-1, 3, -2]
[1, -3, 2]
[1, 2, -3]
[2, -3, 1]
[2, 1, -3]
[3, -2, -1]
[3, -1, -2]
The lexicographically smallest one is [-3, 1, 2].
```

**Example 2:**
```
Input: n = 1, target = 10000000000

Output: []

Explanation:

There are no arrays that sum to 10000000000 and whose absolute values form a permutation of size 1. Therefore, the answer is [].
```
 

**Constraints:**

* `1 <= n <= 10^5`
* `-10^10 <= target <= 10^10`

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 12 ms, Beats 78.57%
Memory: 86.01 MB, Beats 78.57%
```
```c++
class Solution {
public:
    vector<int> lexSmallestNegatedPerm(int n, long long target) {
        vector<int> ans;
        long long maxSum = 1LL * n * (n + 1) / 2;
        if (maxSum < target || -maxSum > target) {
            return {};
        }
        if ((maxSum - target) % 2 != 0) {
            return {};
        }
        vector<bool> used(n + 1);
        for (int i = n; i >= 1; i--){
            if (target <= (maxSum - 2LL * i)){
                ans.push_back(-1 * i);
                maxSum -= 2LL * i;
                used[i] = true;
            }
        }
        for (int i = 1; i <= n; i++){
            if (!used[i]) {
                ans.push_back(i);
            }
        }
        return ans;
    }
};
```
