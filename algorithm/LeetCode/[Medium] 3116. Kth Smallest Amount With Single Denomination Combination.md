3116. Kth Smallest Amount With Single Denomination Combination

You are given an integer array `coins` representing coins of different denominations and an integer `k`.

You have an infinite number of coins of each denomination. However, you are **not allowed** to combine coins of different denominations.

Return the `k`th **smallest** amount that can be made using these coins.

 

**Example 1:**
```
Input: coins = [3,6,9], k = 3

Output: 9

Explanation: The given coins can make the following amounts:
Coin 3 produces multiples of 3: 3, 6, 9, 12, 15, etc.
Coin 6 produces multiples of 6: 6, 12, 18, 24, etc.
Coin 9 produces multiples of 9: 9, 18, 27, 36, etc.
All of the coins combined produce: 3, 6, 9, 12, 15, etc.
```

**Example 2:**
```
Input: coins = [5,2], k = 7

Output: 12

Explanation: The given coins can make the following amounts:
Coin 5 produces multiples of 5: 5, 10, 15, 20, etc.
Coin 2 produces multiples of 2: 2, 4, 6, 8, 10, 12, etc.
All of the coins combined produce: 2, 4, 5, 6, 8, 10, 12, 14, 15, etc.
```
 

**Constraints:**

* `1 <= coins.length <= 15`
* `1 <= coins[i] <= 25`
* `1 <= k <= 2 * 10^9`
* `coins` contains pairwise distinct integers.

# Submissions
---
**Solution 1: (Binary Search, Math, Bitmask, inclusion-exclusion principle)**
```
Runtime: 73 ms
Memory: 19.48 MB
```
```c++
class Solution {
    long long pie(vector<int> &coins, long long x)
    {
        int m = coins.size();
        int nn = (1 << m);
        long long cnt = 0;
        for (int i = 1; i < nn; i++)
        {
            long long lcmm = 1;
            for (int j = 0; j < m; j++)
            {
                if (i & (1 << j))
                {
                    lcmm = lcm(lcmm, coins[j]);
                }
            }
            if (__builtin_popcount(i) & 1)
                cnt += x / lcmm;
            else
                cnt -= x / lcmm;
        }
        return cnt;
    }
public:
    long long findKthSmallest(vector<int>& coins, int k) {
        long long kk = k;
        long long l = 1, r = 1e11, ans = 0;
        while (l <= r)
        {
            long long m = l + (r - l) / 2;
            long long cnt = 0;
            cnt = pie(coins, m);
            if (cnt < kk)
                l = m + 1;
            else
            {
                ans = m;
                r = m - 1;
            }
        }
        return ans;
    }
};
```

**Solution 2: (Binary Search, Math, Bitmask, inclusion-exclusion principle)**
```
Runtime: 7 ms, Beats 93.02%
Memory: 21.76 MB, Beats 12.40%
```
```c++
class Solution {
    long long get(long long x, int m, vector<long long> &lcm, vector<int> &bit_count) {
        long long count = 0;
        for (int mask = 1; mask < m; mask++) {
            if (lcm[mask] > x) {
                continue;
            }
            if (bit_count[mask] & 1) {
                count += x / lcm[mask];
            } else {
                count -= x / lcm[mask];
            }
        }
        return count;
    };
public:
    long long findKthSmallest(vector<int>& coins, int k) {
        int n = coins.size();
        int m = 1 << n;
        sort(coins.begin(), coins.end());
        vector<int> bit_count(m);
        vector<long long> lcm(m);
        long long left = k;
        long long right = 1LL * coins[0] * k + 1;

        for (int mask = 1; mask < m; mask++) {
            long long cur_lcm = 1;
            for (int i = 0; i < n; i++) {
                if (mask >> i & 1) {
                    // cur_lcm * coins[i] = lcm * gcd
                    // cur_lcm / gcd = lcm / coins[i]
                    // ------tmp----
                    //       tmp     * coins[i] = lcm
                    long long tmp = cur_lcm / gcd(cur_lcm, coins[i]);
                    if (tmp <= right / coins[i]) {
                        cur_lcm = tmp * coins[i];
                    } else {
                        cur_lcm = right + 1;
                        break;
                    }
                    bit_count[mask]++;
                }
            }
            lcm[mask] = cur_lcm;
        }

        long long ans;
        while (left <= right) {
            long long mid = (left + right) >> 1;
            if (get(mid, m, lcm, bit_count) < k) {
                left = mid + 1;
            } else {
                ans = right;
                right = mid - 1;
            }
        }
        return left;
    }
};
```

**Solution 3: (Binary Search, Math, Bitmask, inclusion-exclusion principle, optimized)**
```
Runtime: 0 ms Beats 100.00%
Memory: 21.18 MB, Beats 20.16%
```
```c++
class Solution {
    using ll = long long;
public:
    long long findKthSmallest(vector<int>& coins, int k) {
        sort(coins.begin(), coins.end());
        vector<int> new_coins;
        for (int x : coins) {
            bool flag = true;
            for (int y : new_coins) {
                if (x % y == 0) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                new_coins.push_back(x);
            }
        }
        coins = new_coins;

        int n = coins.size();
        int m = (1 << n);
        vector<int> bit_count(m);
        vector<ll> lcm(m, 1);
        ll l = k, r = 1ll * coins[0] * k + 1;

        for (int mask = 1; mask < m; mask++) {
            int pre_mask = mask & (mask - 1);
            int i = __builtin_ctz(mask);

            ll tmp = lcm[pre_mask] / gcd(lcm[pre_mask], coins[i]);
            if (tmp <= r / coins[i]) {
                lcm[mask] = tmp * coins[i];
            } else {
                lcm[mask] = r + 1;
            }
        }

        auto get = [&](ll x) -> ll {
            ll count = 0;
            for (int mask = 1; mask < m; mask++) {
                if (lcm[mask] > x) {
                    continue;
                }
                if (__builtin_popcount(mask) & 1) {
                    count += x / lcm[mask];
                } else {
                    count -= x / lcm[mask];
                }
            }
            return count;
        };

        while (l < r) {
            ll x = (l + r) >> 1;
            if (get(x) >= k) {
                r = x;
            } else {
                l = x + 1;
            }
        }
        return l;
    }
};
```

**Solution 4: (Binary Search, Math, Bitmask, inclusion-exclusion principle)**

    coins = [3,6,9], k = 3
mid:
    3 6 9 12
        ^
cnt
    3 6 9
    3 1 1
    ---    1
      ---  0
    -   -  1
    --0--
    5 - 1 - 0 - 1 + 0 = 3

```
Runtime: 155 ms, Beats 55.04%
Memory: 20.43 MB, Beats 97.67%
```
```c++
class Solution {
    long long check(vector<int> &coins, long long mid) {
        int n = coins.size();
        int m = (1 << n);
        long long cnt = 0;
        for (int mask = 1; mask < m; mask++) {
            long long cur_lcm = 1;
            int k = 0;
            for (int i = 0; i < n; i++) {
                if (mask & (1 << i)) {
                    cur_lcm = lcm(cur_lcm, coins[i]);
                    k += 1;
                }
            }

            // inclusion-exclusion principle
            if (k & 1) {
                cnt += mid / cur_lcm;
            } else {
                cnt -= mid / cur_lcm;
            }
        }
        return cnt;
    }
public:
    long long findKthSmallest(vector<int>& coins, int k) {
        long long left = *min_element(coins.begin(), coins.end());
        long long right = left * k;
        long long ans = 0;
        while (left <= right)
        {
            long long mid = left + (right - left) / 2;
            if (check(coins, mid) < k) {
                left = mid + 1;
            } else {
                ans = mid;
                right = mid - 1;
            }
        }
        return ans;
    }
};```
