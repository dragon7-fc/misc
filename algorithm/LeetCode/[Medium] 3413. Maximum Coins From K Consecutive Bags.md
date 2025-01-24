3413. Maximum Coins From K Consecutive Bags

There are an infinite amount of bags on a number line, one bag for each coordinate. Some of these bags contain coins.

You are given a 2D array `coins`, where` coins[i] = [li, ri, ci]` denotes that every bag from li to ri contains ci coins.

The segments that `coins` contain are non-overlapping.

You are also given an integer `k`.

Return the **maximum** amount of coins you can obtain by collecting k consecutive bags.

 

**Example 1:**
```
Input: coins = [[8,10,1],[1,3,2],[5,6,4]], k = 4

Output: 10

Explanation:

Selecting bags at positions [3, 4, 5, 6] gives the maximum number of coins: 2 + 0 + 4 + 4 = 10.
```

**Example 2:**
```
Input: coins = [[1,10,3]], k = 2

Output: 6

Explanation:

Selecting bags at positions [1, 2] gives the maximum number of coins: 3 + 3 = 6.
```
 

**Constraints:**

* `1 <= coins.length <= 10^5`
* `1 <= k <= 10^9`
* `coins[i] == [li, ri, ci]`
* `1 <= li <= ri <= 10^9`
* `1 <= ci <= 1000`
* The given segments are non-overlapping.

# Submissions
---
**Solution 1: (Sliding Window)**


case 1:
        xxxx  x xxxx
        ----------
        ^^^^
        (most profit)
case 2:
        x x xxx xxxx
         -----------
                ^^^^
                (most profit)

```
Runtime: 89 ms
Memory: 157.91 MB
```
```c++
class Solution {
public:
    long long maximumCoins(vector<vector<int>>& coins, int k) {
        sort(coins.begin(), coins.end());
        int n = coins.size();

        // Start at A[i][0]
        long long res = 0, cur = 0;
        for (int i = 0, j = 0; i < n; ++i) {
            while (j < n && coins[j][1] <= coins[i][0] + k - 1) {
                cur += 1L * (coins[j][1] - coins[j][0] + 1) * coins[j][2];
                j++;
            }
            if (j < n) {
                long long part = 1L * max(0, coins[i][0] + k - 1 - coins[j][0] + 1) * coins[j][2];
                res = max(res, cur + part);
            }
            cur -= 1L * (coins[i][1] - coins[i][0] + 1) * coins[i][2];
        }

        // End at A[i][1]
        cur = 0;
        for (int i = 0, j = 0; i < n; ++i) {
            cur += 1L * (coins[i][1] - coins[i][0] + 1) * coins[i][2];
            while (coins[j][1] < coins[i][1] - k + 1) {
                cur -= 1L * (coins[j][1] - coins[j][0] + 1) * coins[j][2];
                j++;
            }
            long long part = 1L * max(0, coins[i][1] - k - coins[j][0] + 1) * coins[j][2];
            res = max(res, cur - part);
        }

        return res;
    }
};
```
