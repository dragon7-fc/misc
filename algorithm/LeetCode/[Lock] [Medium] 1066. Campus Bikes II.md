1066. Campus Bikes II

On a campus represented as a 2D grid, there are `N` workers and `M` bikes, with `N <= M`. Each worker and bike is a 2D coordinate on this grid.

We assign one unique bike to each worker so that the sum of the Manhattan distances between each worker and their assigned bike is minimized.

The Manhattan distance between two points `p1` and `p2` is `Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|`.

Return the minimum possible sum of Manhattan distances between each worker and their assigned bike.

 

**Example 1:**

![1066_1261_example_1_v2.png](img/1066_1261_example_1_v2.png)
```
Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
Output: 6
Explanation: 
We assign bike 0 to worker 0, bike 1 to worker 1. The Manhattan distance of both assignments is 3, so the output is 6.
```

**Example 2:**

![1066_1261_example_2_v2.png](img/1066_1261_example_2_v2.png)
```
Input: workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
Output: 4
Explanation: 
We first assign bike 0 to worker 0, then assign bike 1 to worker 1 or worker 2, bike 2 to worker 2 or worker 1. Both assignments lead to sum of the Manhattan distances as 4.
```

**Note:**

* `0 <= workers[i][0], workers[i][1], bikes[i][0], bikes[i][1] < 1000`
* All worker and bike locations are distinct.
* `1 <= workers.length <= bikes.length <= 10`

# Submissions
---
**Solution 1: (DP Top-Down)**
```
Runtime: 252 ms
Memory Usage: 15.2 MB
```
```python
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        M, N = len(bikes), len(workers)
        
        def minimum_distance(i,mask):    
            if i == N:
                return 0
            res = float('inf')
            if (i,tuple(mask)) in memo:
                return memo[(i,tuple(mask))]
            for j in range(M):  
                if not mask[j]:
                    mask[j] = 1
                    res = min(res,(abs(workers[i][0]-bikes[j][0])+abs(workers[i][1]-bikes[j][1]))+minimum_distance(i+1,mask))
                    mask[j] = 0  
            memo[(i, tuple(mask))] = res
            return memo[(i, tuple(mask))]
        
        m = [0]*len(bikes)
        memo = {}
        return minimum_distance(0, m)
```

**Solution 2: (DP Top-Down)**
```
Runtime: 76 ms
Memory Usage: 14.6 MB
```
```python
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        M, N = len(bikes), len(workers)
        manhattanDist = lambda i,j: abs(workers[i][0]-bikes[j][0])+abs(workers[i][1]-bikes[j][1])
        dist = []
        for i in range(N):
            dist.append([])
            for j in range(M):
                dist[-1].append(manhattanDist(i,j))
        
        @functools.lru_cache(None)
        def dp(remainingBikes, i):
            if i == N:
                return 0            
            rst = math.inf
            for j in range(len(remainingBikes)):
                rst = min(rst, dist[i][remainingBikes[j]] + dp(remainingBikes[:j] + remainingBikes[j+1:], i+1))
            return rst
        
        return dp(tuple(range(M)), 0)
```

**Solution 3: (Greedy Backtracking, O(M!/(M−N)!))**
```
Runtime: 440 ms
Memory: 9.67 MB
```
```c++
class Solution {
    // Maximum number of bikes is 10
    int smallestDistanceSum = INT_MAX;
    int visited[10];
    
    // Manhattan distance
    int findDistance(vector<int>& worker, vector<int>& bike) {
        return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1]);
    }
    
    void minimumDistanceSum(vector<vector<int>>& workers, int workerIndex, 
                            vector<vector<int>>& bikes, int currDistanceSum) {
        if (workerIndex >= workers.size()) {
            smallestDistanceSum = min(smallestDistanceSum, currDistanceSum);
            return;
        }
        // If the current distance sum is greater than the smallest result 
        // found then stop exploring this combination of workers and bikes
        if (currDistanceSum >= smallestDistanceSum) {
            return;
        }
        
        for (int bikeIndex = 0; bikeIndex < bikes.size(); bikeIndex++) {
            // If bike is available
            if (!visited[bikeIndex]) {
                visited[bikeIndex] = true;
                minimumDistanceSum(workers, workerIndex + 1, bikes, 
                    currDistanceSum + findDistance(workers[workerIndex], bikes[bikeIndex]));
                visited[bikeIndex] = false;
            }
        }
        
    }
public:
    int assignBikes(vector<vector<int>>& workers, vector<vector<int>>& bikes) {
        minimumDistanceSum(workers, 0, bikes, 0);
        return smallestDistanceSum;
    }
};
```

**Solution 4: (Top-Down Dynamic Programming + BitMasking, O(M⋅2^M))**
```
Runtime: 0 ms
Memory: 9.61 MB
```
```c++
class Solution {
    // Maximum value of mask will be 2^(Number of bikes)
    // and number of bikes can be 10 at max
    int memo[1024];
    
    // Manhattan distance
    int findDistance(vector<int>& worker, vector<int>& bike) {
        return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1]);
    }
    
    int minimumDistanceSum(vector<vector<int>>& workers, vector<vector<int>>& bikes, int workerIndex, int mask) {
        if (workerIndex >= workers.size()) {
            return 0;
        }
        
        // If result is already calculated, return it no recursion needed
        if (memo[mask] != -1)
            return memo[mask];
        
        int smallestDistanceSum = INT_MAX;
        for (int bikeIndex = 0; bikeIndex < bikes.size(); bikeIndex++) {
            // Check if the bike at bikeIndex is available
            if ((mask & (1 << bikeIndex)) == 0) {
                // Adding the current distance and repeat the process for next worker
                // also changing the bit at index bikeIndex to 1 to show the bike there is assigned
                smallestDistanceSum = min(smallestDistanceSum, 
                             findDistance(workers[workerIndex], bikes[bikeIndex]) + 
                                          minimumDistanceSum(workers, bikes, workerIndex + 1, 
                                                             mask | (1 << bikeIndex)));
            }
        }
        
        // Memoizing the result corresponding to mask
        return memo[mask] = smallestDistanceSum;
    }
public:
    int assignBikes(vector<vector<int>>& workers, vector<vector<int>>& bikes) {
        // Marking all positions to -1 that signifies result 
        // has not been calculated yet for this mask
        memset(memo, -1, sizeof(memo));
        return minimumDistanceSum(workers, bikes, 0, 0);
    }
};
```

**Solution 5: (Bottom-Up Dynamic Programming + BitMasking, O(M⋅2^M))**
```
Runtime: 2 ms
Memory: 9.47 MB
```
```c++
class Solution {
    // Maximum value of mask will be 2^(Number of bikes)
    // And number of bikes can be 10 at max
    int memo [1024];
    
    // Count the number of ones using Brian Kernighan’s Algorithm
    int countNumOfOnes(int mask) {
        int count = 0;
        while (mask != 0) {
            mask &= (mask - 1);
            count++;
        } 
        return count;
    }
    
    // Manhattan distance
    int findDistance(vector<int>& worker, vector<int>& bike) {
        return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1]);
    }
    
    int minimumDistanceSum(vector<vector<int>>& workers, vector<vector<int>>& bikes) {
        int numOfBikes = bikes.size();
        int numOfWorkers = workers.size();
        int smallestDistanceSum = INT_MAX;

        // 0 signifies that no bike has been assigned and
        // Distance sum for not assigning any bike is equal to 0
        memo[0] = 0;
        // Traverse over all the possible values of mask
        for (int mask = 0; mask < (1 << numOfBikes); mask++) {
            int nextWorkerIndex = countNumOfOnes(mask);
            
            // If mask has more number of 1's than the number of workers
            // Then we can update our answer accordingly
            if (nextWorkerIndex >= numOfWorkers) {
                smallestDistanceSum = min(smallestDistanceSum, memo[mask]);
                continue;
            }
            
            for (int bikeIndex = 0; bikeIndex < numOfBikes; bikeIndex++) {
                // Checking if the bike at bikeIndex has already been assigned
                if ((mask & (1 << bikeIndex)) == 0) {
                    int newMask = (1 << bikeIndex) | mask;
                    
                    // Updating the distance sum for newMask
                    memo[newMask] = min(memo[newMask], memo[mask] + 
                                        findDistance(workers[nextWorkerIndex], bikes[bikeIndex]));
                }
            }
        }
        
        return smallestDistanceSum;
    }
public:
    int assignBikes(vector<vector<int>>& workers, vector<vector<int>>& bikes) {
        // Initializing the answers for all masks to be INT_MAX
        for (int i = 0; i < 1024; i++) {
            memo[i] = INT_MAX;
        }
        return minimumDistanceSum(workers, bikes);
    }
};
```

**Solution 6: (Priority Queue (Similar to Dijkstra's Algorithm), O(P(M,N)⋅log(P(M,N))+(M⋅log(P(M,N))⋅2^M))**
```
Runtime: 18 ms
Memory: 12.78 MB
```
```c++
class Solution {
    // Manhattan distance
    int findDistance(vector<int>& worker, vector<int>& bike) {
        return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1]);
    }
    
    // Count the number of ones using Brian Kernighan’s Algorithm
    int countNumOfOnes(int mask) {
        int count = 0;
        while (mask != 0) {
            mask &= (mask - 1);
            count++;
        } 
        return count;
    }
public:
    int assignBikes(vector<vector<int>>& workers, vector<vector<int>>& bikes) {
        int numOfBikes = bikes.size();
        int numOfWorkers = workers.size();
        
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> priorityQueue;
        unordered_set<int> visited;

        // Initially both distance sum and mask is 0
        priorityQueue.push({0, 0});
        while (!priorityQueue.empty()) {
            int currentDistanceSum = priorityQueue.top().first;
            int currentMask = priorityQueue.top().second;
            priorityQueue.pop();
            
            // Continue if the mask is already traversed
            if (visited.find(currentMask) != visited.end())
                continue;
            
            // Marking the mask as visited
            visited.insert(currentMask);
            // Next Worker index would be equal to the number of 1's in currentMask
            int workerIndex = countNumOfOnes(currentMask);
            
            // Return the current distance sum if all workers are covered
            if (workerIndex == numOfWorkers) {
                return currentDistanceSum;
            }

            for (int bikeIndex = 0; bikeIndex < numOfBikes; bikeIndex++) {
                // Checking if the bike at bikeIndex has been assigned or not
                if ((currentMask & (1 << bikeIndex)) == 0) {
                    int nextStateDistanceSum = currentDistanceSum + 
                        findDistance(workers[workerIndex], bikes[bikeIndex]);
                    
                    // Put the next state pair into the priority queue
                    int nextStateMask = currentMask | (1 << bikeIndex);
                    priorityQueue.push({nextStateDistanceSum, nextStateMask});
                }
            }
        }
        
        // This statement will never be executed provided there is at least one bike per worker
        return -1;
    }
};
```
