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
**Solution 1: (DP Top-down, Time Limit Exceeded)**
```python
import functools
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        ans = -1
        
        @functools.lru_cache(None)
        def dfs(start, cur, amount, length):
            if length > N or amount < 0:
                return -1
            if length == N and amount >= 0:
                return start
            
            amount += gas[cur]
            res = dfs(start, (cur + 1) % N, amount - cost[cur], length + 1)
            return res if res >= 0 else -1
        
        for i in range(N):
            ans = dfs(i, i, 0, 0)
            if ans >= 0:
                return ans
        return ans
```

**Solution 2: (Greedy)**
```
Runtime: 56 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # we will keep track of curr_gas and also
        # of the deficit [+ve means surplus] so that once we have visited all the stations,
        # the deficit will be exactly the distance required to complete the round-trip.
        #   gas: [1,2,3,4,5]
        #  cost: [3,4,5,1,2]
        #  i = 0 , curr_gas = 0, gas_dificit = -2, start = 1
        #  i = 1, curr_gas = 0, gas_dificit = -4, start = 2
        #  i = 2, curr_gas = 0, gas_dificit = -6, start = 3
        #  i = 3, curr_gas = 3, gas_deficit = 3, start = 3
        #  i = 4 , curr_gas = 6, gas_deficit = 6, start = 3
          
        #  now we can see that we can go from 5th station to 1st -> deficit will be 4, then from 1st to 2nd , deficit will be 2, and then from 2nd to 3rd deficit will be 0, thus completing the round-trip. 
        
        curr_gas, gas_dificit = 0, 0
        start_station = 0
        for i in range(len(gas)):
            curr_gas += gas[i] - cost[i]
            gas_dificit += gas[i] - cost[i]
            if curr_gas < 0: #we cannot travel to next station, try to start from next station
                start_station = i+1
                curr_gas = 0  #reset the tank

        return start_station if gas_dificit >= 0 else -1
```