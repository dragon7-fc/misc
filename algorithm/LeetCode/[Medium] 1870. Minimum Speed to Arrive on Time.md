1870. Minimum Speed to Arrive on Time

You are given a floating-point number `hour`, representing the amount of time you have to reach the office. To commute to the office, you must take `n` trains in sequential order. You are also given an integer array dist of length `n`, where `dist[i]` describes the distance (in kilometers) of the `i`th train ride.

Each train can only depart at an integer hour, so you may need to wait in between each train ride.

For example, if the 1^{st} train ride takes `1.5` hours, you must wait for an additional `0.5` hours before you can depart on the 2^{nd} train ride at the 2 hour mark.

Return the **minimum positive integer** speed (**in kilometers per hour**) that all the trains must travel at for you to reach the office on time, or `-1` if it is impossible to be on time.

Tests are generated such that the answer will not exceed 10^7 and hour will have **at most two digits after the decimal point**.

 

**Example 1:**
```
Input: dist = [1,3,2], hour = 6
Output: 1
Explanation: At speed 1:
- The first train ride takes 1/1 = 1 hour.
- Since we are already at an integer hour, we depart immediately at the 1 hour mark. The second train takes 3/1 = 3 hours.
- Since we are already at an integer hour, we depart immediately at the 4 hour mark. The third train takes 2/1 = 2 hours.
- You will arrive at exactly the 6 hour mark.
```

**Example 2:**
```
Input: dist = [1,3,2], hour = 2.7
Output: 3
Explanation: At speed 3:
- The first train ride takes 1/3 = 0.33333 hours.
- Since we are not at an integer hour, we wait until the 1 hour mark to depart. The second train ride takes 3/3 = 1 hour.
- Since we are already at an integer hour, we depart immediately at the 2 hour mark. The third train takes 2/3 = 0.66667 hours.
- You will arrive at the 2.66667 hour mark.
```

**Example 3:**
```
Input: dist = [1,3,2], hour = 1.9
Output: -1
Explanation: It is impossible because the earliest the third train can depart is at the 2 hour mark.
```

**Constraints:**

* `n == dist.length`
* `1 <= n <= 10^5`
* `1 <= dist[i] <= 10^5`
* `1 <= hour <= 10^9`
* There will be at most two digits after the decimal point in `hour`.

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 3596 ms
Memory Usage: 28.3 MB
```
```python
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        lo, hi, n = 1, 10 ** 7 + 1, len(dist)
        while lo < hi:
            speed = lo + (hi - lo) // 2
            need = dist[-1] / speed + sum((dist[i] + speed - 1) // speed for i in range(n - 1))
            if need > hour:
                lo = speed + 1
            else:
                hi = speed
        return -1 if lo == 10 ** 7 + 1 else lo  
```

**Solution 2: (Binary Search)**
```
Runtime: 392 ms
Memory: 101.4 MB
```
```c++
class Solution {
    bool possible(int mid, vector<int> &dist, double hour) {
        int cur = 0;
        for (int i = 0; i < dist.size()-1; i ++) {
            cur += ceil(dist[i]/(double)mid);
        }
        return cur + dist.back()/(double)mid <= hour;
    }
public:
    int minSpeedOnTime(vector<int>& dist, double hour) {
        int n = dist.size(), lo = 1, hi = 1e9, mid;
        while (lo < hi) {
            mid = lo + (hi - lo) / 2;
            if (!possible(mid, dist, hour)) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        if (!possible(lo, dist, hour)) {
            return -1;
        }
        return lo;
    }
};
```
