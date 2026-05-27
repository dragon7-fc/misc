3946. Maximum Number of Items From Sale I

You are given a 2D integer array `items`, where `items[i] = [factori, pricei]` represents the `i`th item. You are also given an integer `budget`.

There are unlimited copies of each item available for purchase.You may buy any number of copies of any items such that the total cost of the purchased copies is at most `budget`.

After buying items, you may receive free copies according to the following rules:

* For each item `i` that you bought **at least one copy** of, you receive one free copy of every item `j` such that `j != i` and `factor_i` divides `factor_j`.
* Buying multiple copies of the same item `i` does not give additional free copies through item `i`.
* The same item `j` can be received multiple times for free if it is received from purchases of different item types.

Return the **maximum** total number of item copies you can obtain, including both purchased copies and free copies, while spending at most `budget` on purchased items.

 

**Example 1:**
```
Input: items = [[6,2],[2,6],[3,4]], budget = 9

Output: 4

Explanation:

You can buy 2 copies of item 0 and 1 copy of item 2 for a total cost of 2 * 2 + 4 = 8, which is not greater than budget = 9.
Buying item 2 gives 1 free copy of item 0, because factor2 = 3 divides factor0 = 6.
You leave with 3 purchased copies and 1 free copy, for a total of 4 item copies.
```

**Example 2:**
```
Input: items = [[2,4],[3,2],[4,1],[6,4],[12,4]], budget = 8

Output: 10

Explanation:

You can buy 1 copy of item 0, 1 copy of item 1, and 2 copies of item 2 for a total cost of 4 + 2 + 2 * 1 = 8.
Buying item 0 gives 1 free copy of items 2, 3, and 4.
Buying item 1 gives 1 free copy of items 3 and 4.
Buying item 2 gives 1 free copy of item 4.
Thus, you receive 6 free copies. You leave with 4 purchased copies and 6 free copies, for a total of 10 item copies.
```

**Constraints:**

* `1 <= items.length <= 1000`
* `items[i] = [factori, pricei]`
* `1 <= factori, pricei <= 1500`
* `1 <= budget <= 1500`

**Solution 1: (DP Bottom-Up, try to add new item for each budget)**
```
Runtime: 293 ms, Beats 15.54%
Memory: 137.96 MB, Beats 11.37%
```
```c++
class Solution {
public:
    int maximumSaleItems(vector<vector<int>>& items, int budget) {
        int n = items.size();
        vector<int> cnt(n);
        for (int i = 0; i < n; i ++) {
            int fi = items[i][0];
            for (int j = 0; j < n; j ++) {
                if (i == j) {
                    continue;
                }
                int fj = items[j][0];
                if (fi % fj == 0) {
                    cnt[j] += 1;
                }
            }
        }
        vector<vector<int>> dp(budget + 1, vector<int>(n + 1));
        for (int i = 1; i <= n; i ++) {
            int price = items[i - 1][1];
            for (int b = 1; b <= budget; b ++) {
                dp[b][i] = dp[b][i - 1];
                if (b >= price) {
                    dp[b][i] = max({dp[b][i],
                                   dp[b - price][i] + 1, 
                                   dp[b - price][i - 1] + cnt[i - 1] + 1});
                }
            }
        }
        return dp[budget][n];
    }
};
````

**Solution 2: (DP Bottom-Up, 1-D)**
```
Runtime: 215 ms, Beats 25.42%
Memory: 35.72 MB, Beats 71.17%
```
```c++
\class Solution {
public:
    int maximumSaleItems(vector<vector<int>>& items, int budget) {
        int n = items.size();
        vector<int> cnt(n);
        for (int i = 0; i < n; i ++) {
            int fi = items[i][0];
            for (int j = 0; j < n; j ++) {
                if (i == j) {
                    continue;
                }
                int fj = items[j][0];
                if (fi % fj == 0) {
                    cnt[j] += 1;
                }
            }
        }
        vector<int> pre(budget + 1), dp(budget + 1);
        for (int i = 1; i <= n; i ++) {
            int price = items[i - 1][1];
            for (int b = 1; b <= budget; b ++) {
                dp[b] = pre[b];
                if (b >= price) {
                    dp[b] = max({dp[b],
                                   dp[b - price] + 1, 
                                   pre[b - price] + cnt[i - 1] + 1});
                }
            }
            pre = dp;
            fill(dp.begin(), dp.end(), 0);
        }
        return pre[budget];
    }
};
```

**Solution 3: (DP Bottom-Up, 1-D optimized)**

    items = [[2,4],[3,2],[4,1],[6,4],[12,4]], budget = 8

dp          0  1  2  3  4  5  6  7  8
      cnt
[2,4]  3    0           4           5
[3,2]  2          3           7     8
[4,1]  1       2     5     6     9 10 < ans 
[6,4]  1                         
[12,4] 0

```
Runtime: 104 ms, Beats 71.37%
Memory: 35.66 MB, Beats 81.01%
```
```c++
class Solution {
public:
    int maximumSaleItems(vector<vector<int>>& items, int budget) {
        int n = items.size();
        vector<int> cnt(n);
        for (int i = 0; i < n; i ++) {
            int fi = items[i][0];
            for (int j = 0; j < n; j ++) {
                if (i == j) {
                    continue;
                }
                int fj = items[j][0];
                if (fi % fj == 0) {
                    cnt[j] += 1;
                }
            }
        }
        vector<int> dp(budget + 1, INT_MIN);
        dp[0] = 0;
        for (int i = 1; i <= n; i ++) {
            int price = items[i - 1][1];
            for (int b = budget; b >= price; b --) {
                dp[b] = max(dp[b], dp[b - price] + cnt[i - 1] + 1);
            }
            for (int b = price; b <= budget; b ++) {
                dp[b] = max(dp[b], dp[b - price] + 1);
            }
        }
        return *max_element(dp.begin(), dp.end());
    }
};
```
