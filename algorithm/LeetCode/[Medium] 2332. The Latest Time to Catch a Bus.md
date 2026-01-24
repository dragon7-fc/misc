2332. The Latest Time to Catch a Bus

You are given a **0-indexed** integer array `buses` of length `n`, where `buses[i]` represents the departure time of the `i`th bus. You are also given a **0-indexed** integer array `passengers` of length `m`, where `passengers[j]` represents the arrival time of the `j`th passenger. All bus departure times are unique. All passenger arrival times are unique.

You are given an integer `capacity`, which represents the maximum number of passengers that can get on each bus.

The passengers will get on the next available bus. You can get on a bus that will depart at `x` minutes if you arrive at `y` minutes where `y <= x`, and the bus is not full. Passengers with the **earliest** arrival times get on the bus first.

Return the latest time you may arrive at the bus station to catch a bus. You **cannot** arrive at the same time as another passenger.

**Note:** The arrays `buses` and `passengers` are not necessarily sorted.

 

**Example 1:**
```
Input: buses = [10,20], passengers = [2,17,18,19], capacity = 2
Output: 16
Explanation: 
The 1st bus departs with the 1st passenger. 
The 2nd bus departs with you and the 2nd passenger.
Note that you must not arrive at the same time as the passengers, which is why you must arrive before the 2nd passenger to catch the bus.
```

**Example 2:**
```
Input: buses = [20,30,10], passengers = [19,13,26,4,25,11,21], capacity = 2
Output: 20
Explanation: 
The 1st bus departs with the 4th passenger. 
The 2nd bus departs with the 6th and 2nd passengers.
The 3rd bus departs with the 1st passenger and you.
```

**Constraints:**

* `n == buses.length`
* `m == passengers.length`
* `1 <= n, m, capacity <= 10^5`
* `2 <= buses[i], passengers[i] <= 10^9`
* Each element in `buses` is unique.
* Each element in `passengers` is unique.

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 786 ms
Memory Usage: 33.6 MB
```
```python
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        passengers.sort()
        cur = 0

        for time in sorted(buses):
            cap = capacity
            while cur < len(passengers) and passengers[cur] <= time and cap > 0:
                cur += 1
                cap -= 1

        best = time if cap > 0 else passengers[cur - 1]

        passengers = set(passengers)
        while best in passengers:
            best -= 1
        return best
```

**Solution 2: (Sort, Greedy)**

                                                 v
    1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
b                              x                             x
p      x                                            x  x  x
      ^^^                                        ^^^^^    

                                                             v
    1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
b                              x                             x                             x
p            x                    x     x                 x     x              x
            ^^^                  ^^^^^^^^^               ^^^^^

```
Runtime: 31 ms, Beats 81.91%
Memory: 80.42 MB, Beats 96.25%
```
```c++
class Solution {
public:
    int latestTimeCatchTheBus(vector<int>& buses, vector<int>& passengers, int capacity) {
        int n = buses.size(), m = passengers.size(), i, j = 0, k, ans;
        sort(begin(buses), end(buses));
        sort(begin(passengers), end(passengers));
        for (i = 0; i < n; i ++) {
            k = 0;
            while (j < m && passengers[j] <= buses[i] && k < capacity) {
                j += 1;
                k += 1;
            }
            if (i == n - 1) { // the last bus
                if (k < capacity) { // still have seats
                    ans = buses[i]; // can be as late as the bus arrive time
                } else { // full of passegers
                    j -= 1;
                    ans = passengers[j] - 1; // should arrive earlier than last passenger aboard
                }
                j -= 1;
                while (j >= 0 && passengers[j] == ans) {
                    j -= 1;
                    ans -= 1;
                }
            }
        }
        return ans;
    }
};
```
