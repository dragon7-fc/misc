2969. Minimum Number of Coins for Fruits II

You are at a fruit market with different types of exotic fruits on display.

You are given a **1-indexed** array `prices`, where `prices[i]` denotes the number of coins needed to purchase the `i`th fruit.

The fruit market has the following offer:

* If you purchase the `i`th fruit at `prices[i]` coins, you can get the next `i` fruits for free.

Note that even if you can take fruit `j` for free, you can still purchase it for `prices[j]` coins to receive a new offer.

Return the **minimum** number of coins needed to acquire all the fruits.

 

**Example 1:**
```
Input: prices = [3,1,2]
Output: 4
Explanation: You can acquire the fruits as follows:
- Purchase the 1st fruit with 3 coins, and you are allowed to take the 2nd fruit for free.
- Purchase the 2nd fruit with 1 coin, and you are allowed to take the 3rd fruit for free.
- Take the 3rd fruit for free.
Note that even though you were allowed to take the 2nd fruit for free, you purchased it because it is more optimal.
It can be proven that 4 is the minimum number of coins needed to acquire all the fruits.
```

**Example 2:**
```
Input: prices = [1,10,1,1]
Output: 2
Explanation: You can acquire the fruits as follows:
- Purchase the 1st fruit with 1 coin, and you are allowed to take the 2nd fruit for free.
- Take the 2nd fruit for free.
- Purchase the 3rd fruit for 1 coin, and you are allowed to take the 4th fruit for free.
- Take the 4th fruit for free.
It can be proven that 2 is the minimum number of coins needed to acquire all the fruits.
```

**Constraints:**

* `1 <= prices.length <= 10^5`
* `1 <= prices[i] <= 10^5`

# Submissions
---
**Solution 1: (DP, Monotonic Queue)**

Intuition
Let dp[i] be the minimum number of coins to buy all the fruites from 0 to i (index starts from 0) and we must buy ith fruit, and thus we can cover all the fruits until i + i + 1 because the last fruite we buy is i.

Then we have
dp[i] = min(dp[j]) + prices[i]
Here
j + j + 1 >= i - 1
and
j < i

Note here, the last fruit we bought is j and we indeed use it to cover the fruits from j + 1 to i - 1 (and we buy i buy ourselves).

If we calculate this directly, the time complexity is O(n ^ 2) which is not acceptable.

The good thing is when i increasing the fesible j values is just in a sliding window (slide to right).

So this is excatly the minimum value in the sliding window which is similar to this problem (https://leetcode.com/problems/minimum-window-substring/).

Btw, although the value of n and prices are as large as 1e5, the result won't be out of 32 bit integer since we only have to buy ~sqrt(n) fruits.

Approach
Use Monotonic Queue to accelerate the DP.

Complexity
Time complexity:
O(n)

Space complexity:
O(n).

               0  1  2
    prices = [ 3, 1, 2]
    dp       [ 3, 4, 5]
    q          0
                  0,1
                     0,1,2
                     x ^
                       dp
```
Runtime: 20 ms, Beats 50.00%
Memory: 120.06 MB, Beats 30.00%
```
```c++
class Solution {
public:
    int minimumCoins(vector<int>& prices) {
        const int n = prices.size();
        vector<int> dp(n);
        deque<int> q;
        dp[0] = prices[0];
        q.push_back(0);
        for (int i = 1; i < n; ++i) {
            dp[i] = dp[q.front()] + prices[i];
            while (!q.empty() && q.front() + q.front() + 1 < i) {
                q.pop_front();
            }
            while (!q.empty() && dp[q.back()] >= dp[i]) {
                q.pop_back();
            }
            q.push_back(i);
        }
        return dp[q.front()];
    }
};
```
