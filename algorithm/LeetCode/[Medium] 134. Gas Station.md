134. Gas Station

There are N gas stations along a circular route, where the amount of gas at station `i` is `gas[i]`.

You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from station `i` to its next station `(i+1)`. You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return `-1`.

**Note:**

* If there exists a solution, it is guaranteed to be unique.
* Both input arrays are non-empty and have the same length.
* Each element in the input arrays is a non-negative integer.

**Example 1:**
```
Input: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
```

**Example 2:**
```
Input: 
gas  = [2,3,4]
cost = [3,4,3]

Output: -1

Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
```

# Submissions
---
**Solution 1: (DFS)**
```python
Runtime: 8440 ms
Memory Usage: 26.7 MB
```
```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        
        def dfs(i, s, r):
            if s == N+1:
                return True
            r += gas[i]
            if cost[i] > r:
                return False
            else:
                return dfs((i+1)%N, s+1, r-cost[i])
            
        
        for i in range(len(gas)):
            if dfs(i, 1, 0):
                return i
        return -1
```

**Solution 2: (Greedy)**

1. If sum of gas is less than sum of cost, then there is no way to get through all stations. So while we loop through the stations we sum up, so that at the end we can check the sum.
1. Otherwise, there must be one unique solution, so the first one I find is the right one. If the tank becomes negative, we restart because that can't happen.

```
Runtime: 56 ms
Memory Usage: 14.6 MB
```
```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if (sum(gas) - sum(cost) < 0):
            return -1
        
        gas_tank, start_index = 0, 0
        
        for i in range(len(gas)):
            gas_tank += gas[i] - cost[i]
            
            if gas_tank < 0:
                start_index = i+1
                gas_tank = 0
            
        return start_index
```

**Solution 3: (One pass)**
```
Runtime: 611 ms
Memory Usage: 18.8 MB
```
```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        total_tank, curr_tank = 0, 0
        starting_station = 0
        for i in range(n):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            # If one couldn't get here,
            if curr_tank < 0:
                # Pick up the next station as the starting one.
                starting_station = i + 1
                # Start with an empty tank.
                curr_tank = 0
        
        return starting_station if total_tank >= 0 else -1
```

**Solution 4: (One pass)**
```
Runtime: 56 ms
Memory Usage: 49.9 MB
```
```c++
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int n = gas.size();

        int total_tank = 0;
        int curr_tank = 0;
        int starting_station = 0;
        for (int i = 0; i < n; ++i) {
          total_tank += gas[i] - cost[i];
          curr_tank += gas[i] - cost[i];
          // If one couldn't get here,
          if (curr_tank < 0) {
            // Pick up the next station as the starting one.
            starting_station = i + 1;
            // Start with an empty tank.
            curr_tank = 0;
          }
        }
        return total_tank >= 0 ? starting_station : -1;
    }
};
```

**Solution 5: (Sliding Window)**
```
Runtime: 774 ms
emory: 19.3 MB
```
```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        i = j = 0
        cur = cnt = 0
        while i < N:
            cur = cur + gas[j] - cost[j]
            j = (j+1)%N
            cnt += 1
            while i < N and cur < 0:
                cur = cur - gas[i] + cost[i]
                cnt -= 1
                i += 1
            if cnt == N:
                break
        return i if i < N else -1
```

**Solution 6: (One pass)**
```
Runtime: 744 ms
Memory: 19.2 MB
```
```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        total = cur = 0
        ans = 0
        for i in range(N):
            total += gas[i] - cost[i]
            cur += gas[i] - cost[i]
            if cur < 0:
                ans = i+1
                cur = 0
        return ans if total >= 0 else -1
```

**Solution 7: (Greedy)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 112.26 MB, Beats 94.29%
```
```c++
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int n = gas.size(), i, j = 0, a, b, cur;
        a = accumulate(gas.begin(), gas.end(), 0);
        b = accumulate(cost.begin(), cost.end(), 0);
        if (a < b) {
            return -1;
        }
        cur = 0;
        for (i = 0; i < n; i ++) {
            cur += gas[i] - cost[i];
            if (cur < 0) {
                cur = 0;
                j = i+1;
            }
        }
        return j;
    }
};
```
