2819. Minimum Relative Loss After Buying Chocolates

You are given an integer array `prices`, which shows the chocolate prices and a 2D integer array `queries`, where `queries[i] = [ki, mi]`.

Alice and Bob went to buy some chocolates, and Alice suggested a way to pay for them, and Bob agreed.

The terms for each query are as follows:

* If the price of a chocolate is less than or equal to `ki`, Bob pays for it.
* Otherwise, Bob pays `ki` of it, and Alice pays the rest.

Bob wants to select **exactly** `mi` chocolates such that his relative loss is minimized, more formally, if, in total, Alice has paid `ai` and Bob has paid `bi`, Bob wants to **minimize** `bi - ai`.

Return an integer array `ans` where `ans[i]` is Bob's minimum relative loss possible for `queries[i]`.

 

**Example 1:**
```
Input: prices = [1,9,22,10,19], queries = [[18,4],[5,2]]
Output: [34,-21]
Explanation: For the 1st query Bob selects the chocolates with prices [1,9,10,22]. He pays 1 + 9 + 10 + 18 = 38 and Alice pays 0 + 0 + 0 + 4 = 4. So Bob's relative loss is 38 - 4 = 34.
For the 2nd query Bob selects the chocolates with prices [19,22]. He pays 5 + 5 = 10 and Alice pays 14 + 17 = 31. So Bob's relative loss is 10 - 31 = -21.
It can be shown that these are the minimum possible relative losses.
```

**Example 2:**
```
Input: prices = [1,5,4,3,7,11,9], queries = [[5,4],[5,7],[7,3],[4,5]]
Output: [4,16,7,1]
Explanation: For the 1st query Bob selects the chocolates with prices [1,3,9,11]. He pays 1 + 3 + 5 + 5 = 14 and Alice pays 0 + 0 + 4 + 6 = 10. So Bob's relative loss is 14 - 10 = 4.
For the 2nd query Bob has to select all the chocolates. He pays 1 + 5 + 4 + 3 + 5 + 5 + 5 = 28 and Alice pays 0 + 0 + 0 + 0 + 2 + 6 + 4 = 12. So Bob's relative loss is 28 - 12 = 16.
For the 3rd query Bob selects the chocolates with prices [1,3,11] and he pays 1 + 3 + 7 = 11 and Alice pays 0 + 0 + 4 = 4. So Bob's relative loss is 11 - 4 = 7.
For the 4th query Bob selects the chocolates with prices [1,3,7,9,11] and he pays 1 + 3 + 4 + 4 + 4 = 16 and Alice pays 0 + 0 + 3 + 5 + 7 = 15. So Bob's relative loss is 16 - 15 = 1.
It can be shown that these are the minimum possible relative losses.
```

**Example 3:**
```
Input: prices = [5,6,7], queries = [[10,1],[5,3],[3,3]]
Output: [5,12,0]
Explanation: For the 1st query Bob selects the chocolate with price 5 and he pays 5 and Alice pays 0. So Bob's relative loss is 5 - 0 = 5.
For the 2nd query Bob has to select all the chocolates. He pays 5 + 5 + 5 = 15 and Alice pays 0 + 1 + 2 = 3. So Bob's relative loss is 15 - 3 = 12.
For the 3rd query Bob has to select all the chocolates. He pays 3 + 3 + 3 = 9 and Alice pays 2 + 3 + 4 = 9. So Bob's relative loss is 9 - 9 = 0.
It can be shown that these are the minimum possible relative losses.
```

**Constraints:**

* `1 <= prices.length == n <= 10^5`
* `1 <= prices[i] <= 10^9`
* `1 <= queries.length <= 10^5`
* `queries[i].length == 2`
* `1 <= ki <= 10^9`
* `1 <= mi <= n`

# Submissions
---
**Solution 1: (Binary Search)**

__Intuition__
Offline process the query. Sort them first. For each query (k, m), we put all the chocolates with price no larger than k on the left side, and all the other chocolates to the right side.

This part can be done by sliding window after sorting the prices.

For the left side, each one contributes the relative diff by its own price.
For the right side, each one contributes the relative diff by k * 2 - its own price.

Clearly we should select the first seveal (cheapest) ones from the left side and the last several (most expensive) ones from right side.

At the very beginning we selected as many as possible on the left side, Note there might be less m chocolates on the left side and in this case we have to select some (the most expensive ones) from the right side anyway.

Then let's replace the selected most expensive one from left side with the unselected most expensive one on the right side as long as it can reduced the relative diff.

Namely, if price[left] > k * 2 - price[right], we should always do the replacment.

Note, both price[left] and price[right] are decreasing (non incresing),
so k * 2 - price[right] is increasing (non decreasing), so we should just stop when finding the first place when price[left'] <= k * 2 - price[right'], namely we can do a binary search on the maximum number of chocolates we can replace.

To calculate the relatvie difference, we just use prefix sum for help since both sides are just sum of conseutive prices (in subarray).

__Complexity__
Time complexity:
O(n + q) where n is the number of chocolates and q is the number of queries.

Space complexity:
O(q(logq + logn)) where n is the number of chocolates and q is the number of queries.


alice       | k
bob         | price - k
alice - bob | k - (price - k) = 2*k - price

    prices = [ 1, 9,22,10,19], queries = [[18,4],[5,2]]
               1  9 10 19 22              [5,2] [18,4]
                  j                        p num
              -num1-     -num2-              = num1 + num2
    sum        0  1 10 20 39 61
```
Runtime: 66 ms, Beats 100.00%
Memory: 99.56 MB, Beats 100.00%
```
```c++
class Solution {
public:
    vector<long long> minimumRelativeLosses(vector<int>& prices, vector<vector<int>>& queries) {
        sort(prices.begin(), prices.end());
        const int n = prices.size();
        vector<long long> sum(n + 1);
        for (int i = 1; i <= n; ++i) {
            sum[i] = sum[i - 1] + prices[i - 1];
        }
        const int m = queries.size();
        vector<int> ind(m);
        for (int i = 0; i < m; ++i) {
            ind[i] = i;
        }
        sort(ind.begin(), ind.end(), [&](const int x, const int y) {
            return queries[x][0] < queries[y][0];
        });
        int j = 0;
        vector<long long> r(m);
        for (int i : ind) {
            const int p = queries[i][0], pp = p << 1, num = queries[i][1];
            for (; j < n && prices[j] <= p; ++j)
            ;
            int num1 = min(num, j);
            int left = 1, right = min(num1, n - num);
            while (left <= right) {
                const int mid = (left + right) >> 1;
                if (prices[num1 - mid] > pp - prices[n - (num - num1) - mid]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
            num1 -= left - 1;
            const long long num2 = num - num1;
            r[i] = num2 * pp - (sum[n] - sum[n - num2]) + sum[num1];
        }
        return r;
    }
};
```
