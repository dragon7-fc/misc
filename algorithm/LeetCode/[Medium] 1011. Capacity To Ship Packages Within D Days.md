1011. Capacity To Ship Packages Within D Days

A conveyor belt has packages that must be shipped from one port to another within `D` days.

The `i`-th package on the conveyor belt has a weight of `weights[i]`.  Each day, we load the ship with packages on the conveyor belt (in the order given by `weights`). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within `D` days.

 

**Example 1:**
```
Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
Explanation: 
A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed. 
```

**Example 2:**
```
Input: weights = [3,2,2,4,1,4], D = 3
Output: 6
Explanation: 
A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
```

**Example 3:**
```
Input: weights = [1,2,3,1,1], D = 4
Output: 3
Explanation: 
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1
```

**Note:**

1. `1 <= D <= weights.length <= 50000`
1. `1 <= weights[i] <= 500`

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 516 ms
Memory Usage: 15.7 MB
```
```python
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def cannot_split(max_wgt):
            s = 0
            days = 1
            for w in weights:
                s += w
                if s > max_wgt:
                    s = w
                    days += 1
            return days > D

        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if cannot_split(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo
```

**Solution 2: (Binary Search)**
```
Runtime: 40 ms
Memory Usage: 8.8 MB
```
```c
bool possible(int k, int *weights, int weightsSize, int days) {
    int cur = k, acc = 1;
    for (int i = 0; i < weightsSize; i ++) {
        cur -= weights[i];
        if (cur < 0) {
            cur = k-weights[i];
            acc += 1;
        }
    }
    return acc <= days;
}

int shipWithinDays(int* weights, int weightsSize, int days){
    int left = 0, right = 0, mid, k;
    for (int i = 0; i < weightsSize; i ++) {
        left = weights[i] > left ? weights[i] : left;
        right += weights[i];
    }
    while (left < right) {
        mid = left + (right-left)/2;
        if (possible(mid, weights, weightsSize, days))
            right = mid;
        else
            left = mid+1;
    }
    return left;
}
```

**Solution 3: (Binary Search)**
```
Runtime: 11 ms, Beats 68.42%
Memory: 34.90 MB, Beats 94.27%
```
```c++
class Solution {
    bool check(int mid, int days, vector<int> &weights) {
        int a = 0, k = 0;
        for (auto &w: weights) {
            if (a + w > mid) {
                k += 1;
                a = w;
            } else {
                a += w;
            }
        }
        k += a != 0;
        return k <= days;
    }
public:
    int shipWithinDays(vector<int>& weights, int days) {
        int left = *max_element(weights.begin(), weights.end()), right = accumulate(weights.begin(), weights.end(), 0), mid, ans = INT_MAX;
        while (left <= right) {
            mid = left + (right - left)/2;
            if (!check(mid, days, weights)) {
                left = mid + 1;
            } else {
                ans = min(ans, mid);
                right = mid - 1;
            }
        }
        return ans;
    }
};
```
