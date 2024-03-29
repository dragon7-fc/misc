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
**Solution 1: (Time Stamp, Greedy Sorted Time Stamp Array)**
```
Runtime: 64 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamp = []
        for trip in trips:
            timestamp.append([trip[1], trip[0]])
            timestamp.append([trip[2], -trip[0]])

        timestamp.sort()

        used_capacity = 0
        for time, passenger_change in timestamp:
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False

        return True
```

**Solution 2: (Bucket Sort)**
```
Runtime: 64 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamp = [0] * 1001
        for trip in trips:
            timestamp[trip[1]] += trip[0]
            timestamp[trip[2]] -= trip[0]

        used_capacity = 0
        for passenger_change in timestamp:
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False

        return True
```

**Solution 3: (Time Stamp, Greedy Sorted Hash Table)**
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

**Solution 4: (Bucket Sort)**
```
Runtime: 22 ms
Memory Usage: 6.4 MB
```
```c

bool carPooling(int** trips, int tripsSize, int* tripsColSize, int capacity){
    int temp[1001] = {0};
    int count = 0;
    for(int i = 0; i < tripsSize; i++)
    {
        temp[trips[i][1]] += trips[i][0];
        temp[trips[i][2]] -= trips[i][0];
    }
    for(int i = 0; i <= 1000; i++)
    {
        count += temp[i];
        if(count > capacity)
            return false;
    }
    return true;
}
```
