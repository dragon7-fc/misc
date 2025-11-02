3733. Minimum Time to Complete All Deliveries

You are given two integer arrays of size 2: `d = [d1, d2]` and `r = [r1, r2]`.

Two delivery drones are tasked with completing a specific number of deliveries. Drone i must complete di deliveries.

Each delivery takes exactly one hour and only one drone can make a delivery at any given hour.

Additionally, both drones require recharging at specific intervals during which they cannot make deliveries. Drone `i` must recharge every `ri` hours (i.e. at hours that are multiples of `ri`).

Return an integer denoting the `minimum` total time (in hours) required to complete all deliveries.

 

**Example 1:**
```
Input: d = [3,1], r = [2,3]

Output: 5

Explanation:

The first drone delivers at hours 1, 3, 5 (recharges at hours 2, 4).
The second drone delivers at hour 2 (recharges at hour 3).
```

**Example 2:**
```
Input: d = [1,3], r = [2,2]

Output: 7

Explanation:

The first drone delivers at hour 3 (recharges at hours 2, 4, 6).
The second drone delivers at hours 1, 5, 7 (recharges at hours 2, 4, 6).
```

**Example 3:**
```
Input: d = [2,1], r = [3,4]

Output: 3

Explanation:

The first drone delivers at hours 1, 2 (recharges at hour 3).
The second drone delivers at hour 3.
```

**Constraints:**

* `d = [d1, d2]`
* `1 <= di <= 10^9`
* `r = [r1, r2]`
* `2 <= ri <= 3 * 10^4`

# Submissions
---
**Solution 1: (Binary Search, Math)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 52.05 MB, Beats 9.09%
```
```c++
class Solution {
    bool check(long long mid, vector<int> &d, vector<int> &r) {
        long long a, b, c;
        a = mid - mid / r[0];
        b = mid - mid / r[1];
        c = mid - mid / lcm(r[0], r[1]);
        return a >= d[0] && b >= d[1] && c >= d[0] + d[1];
    }
public:
    long long minimumTime(vector<int>& d, vector<int>& r) {
        long long left = 1, right = LONG_LONG_MAX, mid, ans;
        while (left <= right) {
            mid = left + (right - left) / 2;
            if (!check(mid, d, r)) {
                left = mid + 1;
            } else {
                ans = mid;
                right = mid - 1;
            }
        }
        return ans;
    }
};
```
