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
