3669. Balanced K-Factor Decomposition

Given two integers `n` and `k`, split the number n into exactly `k` positive integers such that the product of these integers is equal to `n`.

Return any one split in which the **maximum** difference between any two numbers is minimized. You may return the result in any order.

 

**Example 1:**
```
Input: n = 100, k = 2

Output: [10,10]

Explanation:

The split [10, 10] yields 10 * 10 = 100 and a max-min difference of 0, which is minimal.
```

**Example 2:**
```
Input: n = 44, k = 3

Output: [2,2,11]

Explanation:

Split [1, 1, 44] yields a difference of 43
Split [1, 2, 22] yields a difference of 21
Split [1, 4, 11] yields a difference of 10
Split [2, 2, 11] yields a difference of 9
Therefore, [2, 2, 11] is the optimal split with the smallest difference 9.
```
 

**Constraints:**

* `4 <= n <= 10^5`
* `2 <= k <= 5`
* `k` is strictly less than the total number of positive divisors of `n`.

# Submissions
---
**Solution 1: (Backtracking)**
```
Runtime: 67 ms, Beats 39.52%
Memory: 9.68 MB, Beats 69.12%
```
```c++
class Solution {
    vector<int> best;
    int bestDiff = INT_MAX;
    void backtrack(int n, int k, int start, vector<int>& curr) {
        if (k == 1) {
            if (n >= start) {
                curr.push_back(n);
                check(curr);
                curr.pop_back();
            }
            return;
        }

        for (int i = start; i <= n; i++) {
            if (n % i == 0) {
                curr.push_back(i);
                backtrack(n / i, k - 1, i, curr);
                curr.pop_back();
            }
        }
    }

    void check(vector<int>& curr) {
        int mn = *min_element(curr.begin(), curr.end());
        int mx = *max_element(curr.begin(), curr.end());
        if (mx - mn < bestDiff) {
            bestDiff = mx - mn;
            best = curr;
        }
    }
public:
    vector<int> minDifference(int n, int k) {
        vector<int> curr;
        backtrack(n, k, 1, curr);
        return best;
    }
};
```
