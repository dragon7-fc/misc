853. Car Fleet

`N` cars are going to the same destination along a one lane road.  The destination is `target` miles away.

Each car `i` has a constant speed `speed[i]` (in miles per hour), and initial position `position[i]` miles towards the target along the road.

A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.

The distance between these two cars is ignored - they are assumed to have the same position.

A car fleet is some non-empty set of cars driving at the same position and same speed.  Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.


How many car fleets will arrive at the destination?

 

**Example 1:**
```
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 and 8 become a fleet, meeting each other at 12.
The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
The cars starting at 5 and 3 become a fleet, meeting each other at 6.
Note that no other cars meet these fleets before the destination, so the answer is 3.
```

**Note:**

* `0 <= N <= 10 ^ 4`
* `0 < target <= 10 ^ 6`
* `0 < speed[i] <= 10 ^ 6`
* `0 <= position[i] < target`
* All initial positions are different.

# Solution
---
## Approach 1: Sort
**Intuition**

Call the "lead fleet" the fleet furthest in position.

If the car `S` (Second) behind the lead car `F` (First) would arrive earlier, then `S` forms a fleet with the lead car `F`. Otherwise, fleet `F` is final as no car can catch up to it - cars behind `S` would form fleets with `S`, never `F`.

**Algorithm**

A car is a `(position, speed)` which implies some arrival time `(target - position) / speed`. Sort the cars by position.

Now apply the above reasoning - if the lead fleet drives away, then count it and continue. Otherwise, merge the fleets and continue.

```python
class Solution(object):
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed))
        times = [float(target - p) / s for p, s in cars]
        ans = 0
        while len(times) > 1:
            lead = times.pop()
            if lead < times[-1]: ans += 1  # if lead arrives sooner, it can't be caught
            else: times[-1] = lead # else, fleet arrives at later time 'lead'

        return ans + bool(times) # remaining car is fleet (if it exists)
```

**Complexity Analysis**

* Time Complexity: $O(N \log N)$, where $N$ is the number of cars. The complexity is dominated by the sorting operation.

* Space Complexity: $O(N)$, the space used to store information about the cars.

# Solution
---
**Solution 1: (Sort)**
```
Runtime: 376 ms
Memory Usage: 16.1 MB
```
```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        times = [float(target - p) / s for p, s in cars]
        ans = 0
        while len(times) > 1:
            lead = times.pop()
            if lead < times[-1]: ans += 1  # if lead arrives sooner, it can't be caught
            else: times[-1] = lead # else, fleet arrives at later time 'lead'

        return ans + bool(times) # remaining car is fleet (if it exists)
```

**Solution 2: (Sort, forward)**
```
Runtime: 80 ms
Memory Usage: 20.6 MB
```
```c++
class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int, int>> vec;
        
        for (int i = 0; i < position.size(); ++i)
            vec.emplace_back(position[i], speed[i]);
        
        sort(vec.begin(), vec.end(), [](const auto& a, const auto& b) {
            return a.first > b.first;
        });
        
        double prevTime = 0;
        int fleets = position.size();
        
        for (int i = 0; i < position.size(); ++i) {
            double curTime = ((double)target - vec[i].first) / vec[i].second;
            if (curTime <= prevTime)  // faster in a group
                --fleets;
            prevTime = max(prevTime, curTime);
        }
        
        return fleets;
    }
};
```

**Solution 3: (Sort, backward)**

```
Runtime: 284 ms
Memory Usage: 16.3 MB
```
```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        times = [(target - p) / s for p, s, in cars]
        # count from back
        most = 0
        count = 0
        for i in range(len(times)-1 ,-1, -1):
            if times[i] > most:  // slower in a group
                most = times[i]
                count += 1
                
        return count
```
