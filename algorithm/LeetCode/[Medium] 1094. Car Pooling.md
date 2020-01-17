1094. Car Pooling

You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle **only** drives east (ie. it **cannot** turn around and drive west.)

Given a list of `trips`, `trip[i] = [num_passengers, start_location, end_location]` contains information about the `i`-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

Return `true` if and only if it is possible to pick up and drop off all passengers for all the given trips. 

 

**Example 1:**
```
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
```

**Example 2:**
```
Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
```

**Example 3:**
```
Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true
```

**Example 4:**
```
Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output: true
```
 

**Constraints:**

* `trips.length <= 1000`
* `trips[i].length == 3`
* `1 <= trips[i][0] <= 100`
* `0 <= trips[i][1] < trips[i][2] <= 1000`
* `1 <= capacity <= 100000`

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 64 ms
Memory Usage: 13.2 MB
```
```python
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # each item in station is: one station: number of passengers picked up or dropped off
        # note: each station could pick up and drop off at the same time
        station = collections.defaultdict(list)
        
        for i in trips:
            # at time i[1], the car stops and pick up passenger, so we have positive i[0]
            station[i[1]].append(i[0])
            # at time i[2], the car stops and drops off passenger, so we have negative i[0]
            station[i[2]].append(-i[0])
        
        # sort the station by time
        station = sorted(station.items(), key = lambda x:x[0])

        count = 0
        for i in station:
            # count the passenger in the car at this station
            for j in i[1]:
                count = count+j
            if count>capacity:
                return False
        return True
```